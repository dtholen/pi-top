#include <iostream>

main()
{
    int res = system("echo \"from usb.core import find as finddev; dev=finddev(idVendor=<vendor_id>,idProduct=<product_id>); dev.reset()\" | python3");

    return res;
}
