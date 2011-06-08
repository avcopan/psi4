#include <stdio.h>
#include "libint.h"
#include "vrr_header.h"

  /* Computes quartets necessary to compute (pp|ff) integrals */

void vrr_order_ppff(Libint_t * Libint, prim_data *Data)
{
 REALTYPE *vrr_stack = Libint->vrr_stack;
 REALTYPE *tmp, *target_ptr;
 int i, am[2];
 _BUILD_00p0(Data,vrr_stack+0, Data->F+2, Data->F+3, NULL, NULL, NULL);
 _BUILD_00p0(Data,vrr_stack+3, Data->F+3, Data->F+4, NULL, NULL, NULL);
 _BUILD_00d0(Data,vrr_stack+6, vrr_stack+0, vrr_stack+3, Data->F+2, Data->F+3, NULL);
 _BUILD_00p0(Data,vrr_stack+12, Data->F+1, Data->F+2, NULL, NULL, NULL);
 _BUILD_00d0(Data,vrr_stack+15, vrr_stack+12, vrr_stack+0, Data->F+1, Data->F+2, NULL);
 _BUILD_p0d0(Data,vrr_stack+21, vrr_stack+15, vrr_stack+6, NULL, NULL, vrr_stack+0);
 _BUILD_00f0(Data,vrr_stack+39, vrr_stack+15, vrr_stack+6, vrr_stack+12, vrr_stack+0, NULL);
 _BUILD_00p0(Data,vrr_stack+49, Data->F+0, Data->F+1, NULL, NULL, NULL);
 _BUILD_00d0(Data,vrr_stack+52, vrr_stack+49, vrr_stack+12, Data->F+0, Data->F+1, NULL);
 _BUILD_00f0(Data,vrr_stack+58, vrr_stack+52, vrr_stack+15, vrr_stack+49, vrr_stack+12, NULL);
 _BUILD_00p0(Data,vrr_stack+12, Data->F+4, Data->F+5, NULL, NULL, NULL);
 _BUILD_00d0(Data,vrr_stack+68, vrr_stack+3, vrr_stack+12, Data->F+3, Data->F+4, NULL);
 _BUILD_00f0(Data,vrr_stack+74, vrr_stack+6, vrr_stack+68, vrr_stack+0, vrr_stack+3, NULL);
 _BUILD_p0f0(Data,vrr_stack+84, vrr_stack+39, vrr_stack+74, NULL, NULL, vrr_stack+6);
 _BUILD_p0f0(Data,vrr_stack+114, vrr_stack+58, vrr_stack+39, NULL, NULL, vrr_stack+15);
   tmp = vrr_stack + 114;
   target_ptr = Libint->vrr_classes[1][3];
   for(i=0;i<30;i++)
     target_ptr[i] += tmp[i];
 _BUILD_00g0(Data,vrr_stack+144, vrr_stack+39, vrr_stack+74, vrr_stack+15, vrr_stack+6, NULL);
 _BUILD_00g0(Data,vrr_stack+159, vrr_stack+58, vrr_stack+39, vrr_stack+52, vrr_stack+15, NULL);
 _BUILD_00p0(Data,vrr_stack+0, Data->F+5, Data->F+6, NULL, NULL, NULL);
 _BUILD_00d0(Data,vrr_stack+15, vrr_stack+12, vrr_stack+0, Data->F+4, Data->F+5, NULL);
 _BUILD_00f0(Data,vrr_stack+174, vrr_stack+68, vrr_stack+15, vrr_stack+3, vrr_stack+12, NULL);
 _BUILD_00g0(Data,vrr_stack+184, vrr_stack+74, vrr_stack+174, vrr_stack+6, vrr_stack+68, NULL);
 _BUILD_p0g0(Data,vrr_stack+199, vrr_stack+144, vrr_stack+184, NULL, NULL, vrr_stack+74);
 _BUILD_p0g0(Data,vrr_stack+244, vrr_stack+159, vrr_stack+144, NULL, NULL, vrr_stack+39);
   tmp = vrr_stack + 244;
   target_ptr = Libint->vrr_classes[1][4];
   for(i=0;i<45;i++)
     target_ptr[i] += tmp[i];
 _BUILD_00h0(Data,vrr_stack+289, vrr_stack+144, vrr_stack+184, vrr_stack+39, vrr_stack+74, NULL);
 _BUILD_00h0(Data,vrr_stack+310, vrr_stack+159, vrr_stack+144, vrr_stack+58, vrr_stack+39, NULL);
 _BUILD_00p0(Data,vrr_stack+3, Data->F+6, Data->F+7, NULL, NULL, NULL);
 _BUILD_00d0(Data,vrr_stack+6, vrr_stack+0, vrr_stack+3, Data->F+5, Data->F+6, NULL);
 _BUILD_00f0(Data,vrr_stack+331, vrr_stack+15, vrr_stack+6, vrr_stack+12, vrr_stack+0, NULL);
 _BUILD_00g0(Data,vrr_stack+341, vrr_stack+174, vrr_stack+331, vrr_stack+68, vrr_stack+15, NULL);
 _BUILD_00h0(Data,vrr_stack+356, vrr_stack+184, vrr_stack+341, vrr_stack+74, vrr_stack+174, NULL);
 _BUILD_p0h0(Data,vrr_stack+377, vrr_stack+289, vrr_stack+356, NULL, NULL, vrr_stack+184);
 _BUILD_p0h0(Data,vrr_stack+440, vrr_stack+310, vrr_stack+289, NULL, NULL, vrr_stack+144);
   tmp = vrr_stack + 440;
   target_ptr = Libint->vrr_classes[1][5];
   for(i=0;i<63;i++)
     target_ptr[i] += tmp[i];
 _BUILD_00i0(Data,vrr_stack+503, vrr_stack+289, vrr_stack+356, vrr_stack+144, vrr_stack+184, NULL);
 _BUILD_00i0(Data,vrr_stack+531, vrr_stack+310, vrr_stack+289, vrr_stack+159, vrr_stack+144, NULL);
 _BUILD_00p0(Data,vrr_stack+12, Data->F+7, Data->F+8, NULL, NULL, NULL);
 _BUILD_00d0(Data,vrr_stack+68, vrr_stack+3, vrr_stack+12, Data->F+6, Data->F+7, NULL);
 _BUILD_00f0(Data,vrr_stack+74, vrr_stack+6, vrr_stack+68, vrr_stack+0, vrr_stack+3, NULL);
 _BUILD_00g0(Data,vrr_stack+559, vrr_stack+331, vrr_stack+74, vrr_stack+15, vrr_stack+6, NULL);
 _BUILD_00h0(Data,vrr_stack+0, vrr_stack+341, vrr_stack+559, vrr_stack+174, vrr_stack+331, NULL);
 _BUILD_00i0(Data,vrr_stack+559, vrr_stack+356, vrr_stack+0, vrr_stack+184, vrr_stack+341, NULL);
 _BUILD_p0i0(Data,vrr_stack+587, vrr_stack+503, vrr_stack+559, NULL, NULL, vrr_stack+356);
 _BUILD_p0i0(Data,vrr_stack+671, vrr_stack+531, vrr_stack+503, NULL, NULL, vrr_stack+289);
   tmp = vrr_stack + 671;
   target_ptr = Libint->vrr_classes[1][6];
   for(i=0;i<84;i++)
     target_ptr[i] += tmp[i];
 _BUILD_d0f0(Data,vrr_stack+755, vrr_stack+114, vrr_stack+84, vrr_stack+58, vrr_stack+39, vrr_stack+21);
   tmp = vrr_stack + 755;
   target_ptr = Libint->vrr_classes[2][3];
   for(i=0;i<60;i++)
     target_ptr[i] += tmp[i];
 _BUILD_d0g0(Data,vrr_stack+815, vrr_stack+244, vrr_stack+199, vrr_stack+159, vrr_stack+144, vrr_stack+84);
   tmp = vrr_stack + 815;
   target_ptr = Libint->vrr_classes[2][4];
   for(i=0;i<90;i++)
     target_ptr[i] += tmp[i];
 _BUILD_d0h0(Data,vrr_stack+0, vrr_stack+440, vrr_stack+377, vrr_stack+310, vrr_stack+289, vrr_stack+199);
   tmp = vrr_stack + 0;
   target_ptr = Libint->vrr_classes[2][5];
   for(i=0;i<126;i++)
     target_ptr[i] += tmp[i];
 _BUILD_d0i0(Data,vrr_stack+126, vrr_stack+671, vrr_stack+587, vrr_stack+531, vrr_stack+503, vrr_stack+377);
   tmp = vrr_stack + 126;
   target_ptr = Libint->vrr_classes[2][6];
   for(i=0;i<168;i++)
     target_ptr[i] += tmp[i];

}
