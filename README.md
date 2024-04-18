# SMPPTF Small Tools

When get new IBM z patches or PTFs (Program Temporary Fixes) from the IBM ShopZ web, the downloaded package is supposed to be saved on a z/OS USS folder then apply through GIMSMP these PTFs from There. These programs serve as an alternative to that normal approach.

Instead of applying PTFs from the USS folder, this set of programs on the client (Windows or MAC) does some checking, reducing and formatting. Then the final results are 80-column SMPHOLD and SMPPTFIN that can be directly binary transferred to an 80-column sequential or PDS member on the z/OS and apply the PTFs there. Allocating disk space, creating and manipulating a USS folder are no longer needed during the whole process.   

However, a 7-zip on the client (Windows or MAC) should be used to unpack the PTF package file(s) -- the single SMPPTFIN zipped file in pax.Z format from IBM ShopZ will be cut into several files each with a size no more than 512MB.

1. ***SMPPTFIN_PAX_Merger.py*** is used to merge all cut files downloaded from ShopZ into a single pax.Z file.

2. ***SMPPTFIN_Splitter.py*** is used to split the single binary file (in EBCDIC) named **SMPPTFIN"" into several binary files each a self-content applicable PTF. All the split PTFs are in the folder as **SMPPTFIN**.
   2.1. Before running **SMPPTFIN_Splitter.py**, you will have to use 7-zip twice to unpack the pax.Z to a pax first then unpack the pax to a binary file: SMPPTFIN.
   
3. ***SMPPTFIN_Check_PTF_Exists.py*** is used to check if some of the PTFs that have been split from item 2 described above are already applied. All of the applied will be deleted from the folder.

4. ***SMPPTFIN_IF_REQ.py*** is used to check and list -- if there is any -- all Corequisites or Co-required PTFs for different FMIDs but have to applied at the same time with the very single file: **SMPPTFIN**. 
   4.1. You have to list all your installed products' FMIDs in the program.
   4.2. If any Corequisites are found, you have to do the same ShopZ actions again to download these extra PTFs.
   
5. ***SMPPTFIN_IF_REQ_for_Folder.py*** is used to check and list -- if there is any -- all Corequisites or Co-required PTFs of different FMIDs but have to applied at the same time with all PTFs extracted from **SMPPTFIN** under the same folder. 
   5.1. You have to list all your installed products' FMIDs in the program.
   5.2. If any Corequistes are found, you have to do the same ShopZ actions again to download these extra PTFs.


6. ***SMPPTFIN_Combine_All_to_One_SMPPTFIN.py*** is used to combine all split PTFs into a single file so you don't have to upload each single PTFs, just upload this combined single file in binary-mode for applying.
   
7. ***SMPHOLD_Display.py*** is used to create an ASCII file of the **SMPHOLD** file on the client, so you may read the **SMPHOLD** without having to upload it to z/OS first. The **SMPHOLD** file, however, has to be uploaded as the one of the input for the SMP/E RECEIVE process

8. ***SMPPTFIN_Header_Display.py*** is used to display the descriptive portion in the very beginning of a single PTF file or the SMPPTFIN itself. 

9. ***SMPPTFIN_Header_Dsiplay_for_Folder.py*** is used to display the first few lines of description of each PTF file in the same folder.
