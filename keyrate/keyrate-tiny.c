/*
 * Version of keyrate that doesn't use C library functions so we can build with
 * libctiny to get an ultra minimal executable size.
 */

#include <windows.h>
#include <limits.h>

BOOL strtoi(char *s, DWORD* rv)
{
   DWORD result = 0; 
   DWORD oldresult;

   while (*s == '0') s++;

   while (*s) {
      int digit = *s++ - '0';
      if (digit < 0 || 9 < digit) 
         return FALSE;
      oldresult = result;
      result *= 10;
      result += digit;

      /* detect overflow */
      if (oldresult > result) {
         result = INT_MAX;
         break;
      }
   }
   *rv = result;
   return TRUE;
}

void print(DWORD out, const char* msg)
{
   WriteConsole(GetStdHandle(out), msg, strlen(msg), NULL, NULL); 
}

int main(int argc, char* argv[])
{
   FILTERKEYS fk = { sizeof(FILTERKEYS) };

   if (argc == 3 
         && strtoi(argv[1], &fk.iDelayMSec) 
         && strtoi(argv[2], &fk.iRepeatMSec))
   {
      fk.dwFlags = FKF_FILTERKEYSON|FKF_AVAILABLE;
   }
   else
   {
      print(STD_OUTPUT_HANDLE,
           "Usage: keyrate <delay ms> <repeat ms>\n"
           "No parameters given: disabling.");
   }

   if (!SystemParametersInfo(SPI_SETFILTERKEYS, 0, (LPVOID) &fk, 0))
   {
      print(STD_ERROR_HANDLE,
           "SystemParametersInfo(SPI_SETFILTERKEYS,..) failed.\n"
           "Unable to set keyrate.");
   }

   return 0;
}
