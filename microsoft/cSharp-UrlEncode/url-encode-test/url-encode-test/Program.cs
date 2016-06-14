using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Web;

namespace url_encode_test
{
    class Program
    {
        static void Main(string[] args)
        {
            string url = "http://deblugger/Home/Search?q=" + Uri.EscapeDataString("berugram,burdwan,west bengal") + "+&la=22.57054&lo=88.37124&uln=" + Uri.EscapeDataString("Kolkata, India") + "&mf=en-in&cf=&rf=BLU&vf=&ec=" + Uri.EscapeDataString("BLU@enin:Default20100527_VS.QasDsX");
            //url = Uri.EscapeDataString(url);

            Console.WriteLine(url);
        }
    }
}
