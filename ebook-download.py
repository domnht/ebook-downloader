import os
import wget
import img2pdf
import datetime

class Book(object):
    def __init__(self, name, code):
        self.code = code
        self.name = name

    def makeUrl(self, page):
        url = "http://cdnelearning.nxbgd.vn/uploads/books/{}-{}.jpg" # hanhtrangso
        return url.format(self.code, page)

    def makeFileName(self, page):
        name = "{} trang {}.jpg"
        return name.format(self.name, page)

    def download(self, page):
        url = self.makeUrl(page)
        fileName = self.makeFileName(page)
        try:
            wget.download(url, fileName)
            return True
        except:
            return False

    def save(self):
        # Check if code is empty
        if self.code == "":
            print("{}: Book code is invalid!\n".format(self.name))
            return

        # Create and go to temporary folder to save downloaded images (jpg)
        temp = self.name + " @ " + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        os.mkdir(temp)
        os.chdir(temp)

        # Start to download images
        print("{}: Start to download…".format(self.name))
        page = 0
        images = []
        while self.download(page + 1):
            page += 1
            # Add file name to list, which will be used to create PDF
            images.append(self.makeFileName(page))

        # In case no data was downloaded
        if page == 0:
            print("No data found, please try again later!\n")
            # Go back to begin directory
            os.chdir("..")
            # Delete the created temporary folder
            os.rmdir(temp)
            return

        # Inform user the number of downloaded pages
        print("Downloaded {} page(s).".format(page))

        # Convert all JPG to one PDF
        print("Converting to PDF…")
        outputFileName = self.name + ".pdf"
        with open(outputFileName, "wb") as file:
            file.write(img2pdf.convert(images))

        # Delete downloaded images
        print("Cleaning temporary…")
        for image in images: os.remove(image)

        # Move PDF file to begin directory, and go back
        os.rename(outputFileName, "../" + outputFileName)
        os.chdir("..")

        # Delete the created temporary folder
        os.rmdir(temp)

        print("The book \"{}\" saved!\n".format(self.name))

class BookCD(Book):
    def makeUrl(self, page):
        url = "http://hvegjijo7jobj.vcdn.cloud/E_Learning/page/{}_{}.jpg"
        return url.format(page, self.code)


books = [
    # TOAN 6
    # Chan troi sang tao
    # Book("SGK Toan 6 tap 1 CTST", "10783_20220414090925_wm_shs-toan-6---tap-1---tb1"),
    # Book("SGK Toan 6 tap 2 CTST", "10784_20220414091036_wm_shs-toan-6---tap-2---tb1"),
    # Book("SBT Toan 6 tap 1 CTST", "10843_20210609031618_wm_bt-toan-6-tap-1"),
    # Book("SBT Toan 6 tap 2 CTST", "10844_20210609031703_wm_bt-toan-6-tap-2"),
    # Book("SGV Toan 6 CTST", "10863_20210609034739_wm_sgv-toan-6"),
    # Ket noi tri thuc
    # Book("SGK Toan 6 tap 1 KNTT", "10741_20220414084356_wm_shs-toan-6---tap-1---tb1"),
    # Book("SGK Toan 6 tap 2 KNTT", "10742_20220414084441_wm_shs-toan-6---tap-2---tb1"),
    # Book("SBT Toan 6 tap 1 KNTT", "10831_20210609025409_wm_bt-toan-6-tap-1"),
    # Book("SBT Toan 6 tap 2 KNTT", "10832_20210609025647_wm_bt-toan-6-tap-2"),
    # Book("SGV Toan 6 KNTT", "10876_20210610035524_wm_sgv-toan-6"),
    # Canh dieu
    # Book("SGK Toan 6 tap 1 CD", ""), # Link khac Toan 7
    # Book("SGK Toan 6 tap 2 CD", ""), # Link khac Toan 7
    # Book("SBT Toan 6 tap 1 CD", ""), # Khong public
    # Book("SBT Toan 6 tap 2 CD", ""), # Khong public
    # Book("SGV Toan 6 CD", ""), # Link khac Toan 7

    # HOAT DONG TRAI NGHIEM, HUONG NGHIEP 6
    # Chan troi sang tao
    # Book("SGK HDTN, HN 6 CTST", "10792_20220414085236_wm_shs-hoat-dong-trai-nghiem-huong-nghiep---tb1"),
    # Book("SBT HDTN, HN 6 CTST", "10836_20210819055926_wm_bt-hoat-dong-trai-nghiem-huong-nghiep-6"),
    # Book("SGV HDTN, HN 6 CTST", "10857_20210819055958_wm_sgv-hoat-dong-trai-nghiem-huong-nghiep-6"),

    # TOAN 7
    # Chan troi sang tao
    # Book("SGK Toan 7 tap 1 CTST", "11014_20220518081658_wm_shs-toan-7---tap-1"),
    # Book("SGK Toan 7 tap 2 CTST", "11015_20220518082004_wm_shs-toan-7---tap-2"),
    # Book("SBT Toan 7 tap 1 CTST", "11241_20220629110934_wm_sbt-toan-7---tap-1"),
    # Book("SBT Toan 7 tap 2 CTST", "11242_20220629111126_wm_sbt-toan-7---tap-2"),
    # Book("SGV Toan 7 CTST", "11228_20220629110741_wm_sgv-toan-7"),
    # Ket noi tri thuc
    # Book("SGK Toan 7 tap 1 KNTT", "10993_20220517041308_wm_shs-toan-7---tap-1"),
    # Book("SGK Toan 7 tap 2 KNTT", "10994_20220517041527_wm_shs-toan-7---tap-2"),
    # Book("SBT Toan 7 tap 1 KNTT" ,"11201_20220629092408_wm_sbt-toan-7---tap-1"),
    # Book("SBT Toan 7 tap 2 KNTT" ,"11204_20220629092815_wm_sbt-toan-7---tap-2"),
    # Book("SGV Toan 7 KNTT", ""),
    # Canh dieu
    # Book("SGK Toan 7 tap 1 CD", "Toan7T1_29_03_2022_v13"),
    # Book("SGK Toan 7 tap 2 CD", "Toan7T2_29_03_2022_v13"),
    # Book("SBT Toan 7 tap 1 CD", ""), # Khong public
    # Book("SBT Toan 7 tap 2 CD", ""), # Khong public
    # Book("SGV Toan 7 CD", "SGVToan7_22_06_2022_v1"),

    # TOAN 10
    # Chan troi sang tao
    # Book("SGK Toan 10 tap 1 CTST", "11093_20220518082650_wm_shs-toan-10---tap-1"),
    # Book("SGK Toan 10 tap 2 CTST", "11094_20220518082726_wm_shs-toan-10---tap-2"),
    # Book("SBT Toan 10 tap 1 CTST", "11297_20220715084718_wm_sbt-toan-10---tap-1"),
    # Book("SBT Toan 10 tap 2 CTST", "11298_20220715090026_wm_sbt-toan-10---tap-2"),
    # Book("SGV Toan 10 CTST", "11206_20220623085743_wm_sgv-toan-10"),
    # Book("Chuyen de Toan 10 CTST", "11096_20220518082808_wm_chuyen-de-toan-10"),
    # Book("SGV chuyen de Toan 10 CTST", "11207_20220623091017_wm_sgv-chuyen-de-hoc-tap-toan-10"),
    # Ket noi tri thuc
    # Book("SGK Toan 10 tap 1 KNTT", "11011_20220527025139_wm_shs-toan-10---tap-1"),
    # Book("SGK Toan 10 tap 2 KNTT", "11012_20220527025203_wm_shs-toan-10---tap-2"),
    # Book("SBT Toan 10 tap 1 KNTT", "11140_20220627041934_wm_sbt-toan-10---tap-1"),
    # Book("SBT Toan 10 tap 2 KNTT", "11141_20220627042411_wm_sbt-toan-10---tap-2"),
    # Book("SGV Toan 10 KNTT", ""),
    # Book("Chuyen de Toan 10 KNTT", "11013_20220527025233_wm_chuyen-de-hoc-tap-toan-10"),
    # Book("SGV chuyen de Toan 10 KNTT", "11139_20220627041607_wm_sgv-chuyen-de-hoc-tap-toan-10"),
    # Canh dieu
    # BookCD("SGK Toan 10 tap 1 CD", "Toan10T1_07_04_2022_v20"),
    # BookCD("SGK Toan 10 tap 2 CD", "Toan10T2_07_04_2022_v20"),
    # BookCD("Chuyen de Toan 10 CD", "CDToan10_07_04_2022_v20"),
    # BookCD("SBT Toan 10 tap 1 CD", ""), # Khong public
    # BookCD("SBT Toan 10 tap 2 CD", ""), # Khong public
    # BookCD("SGV Toan 10 CD", "SGVToan10_22_06_2022_v1"),
    # BookCD("SGV chuyen de Toan 10 CD", ""), # Khong public

    # HOAT DONG TRAI NGHIEM, HUONG NGHIEP 7
    # Chan troi sang tao
    # Book("SGK HDTN, TN 7 CTST1", "11024_20220517052957_wm_shs-hoat-dong-trai-nghiem-huong-nghiep-ban-1"),
    # Book("SBT HDTN, TN 7 CTST1", "11232_20220629101801_wm_sbt-hoat-dong-trai-nghiem-huong-nghiep-7---ban-1"),
    # Book("SGV HDTN, TN 7 CTST1", "11215_20220629101447_wm_sgv-hoat-dong-trai-nghiem-huong-nghiep---ban-1"),

    # NGU VAN 7
    # Book("SGK Ngu van 7 tap 1 CTST", "11017_20220517054019_wm_shs-ngu-van-7---tap-1"),
    # Book("SGK Ngu van 7 tap 2 CTST", "11018_20220518081345_wm_shs-ngu-van-7---tap-2"),
    # Book("SBT Ngu van 7 tap 1 CTST", "11239_20220629105904_wm_sbt-ngu-van-7---tap-1"),
    # Book("SBT Ngu van 7 tap 2 CTST", "11240_20220629110138_wm_sbt-ngu-van-7---tap-2"),
    # Book("SGV Ngu van 7 tap 1 CTST", "11225_20220629105435_wm_sgv-ngu-van-7---tap-1"),
    # Book("SGV Ngu van 7 tap 2 CTST", "11226_20220629105642_wm_sgv-ngu-van-7---tap-2"),

    # GIAO DUC CONG DAN 7
    # Book("SGK GDCD 7 CTST", "11027_20220517052337_wm_shs-giao-duc-cong-dan-7"),
    # Book("SBT GDCD 7 CTST", "11231_20220629100900_wm_sbt-giao-duc-cong-dan-7"),
    # Book("SGV GDCD 7 CTST", "11210_20220629100649_wm_sgv-giao-duc-cong-dan-7"),

    # VAT LY 10
    # Book("SGK Vat ly 10 CTST", "11097_20220518085404_wm_shs-vat-li-10"),
    # Book("SBT Vat ly 10 CTST", "11217_20220623105529_wm_sbt-vat-li-10"),
    # Book("SGV Vat ly 10 CTST", "11214_20220623103315_wm_sgv-vat-li-10"),
    # Book("Chuyen de Vat ly 10 CTST", "11098_20220518085435_wm_chuyen-de-hoc-tap-vat-li-10"),
    # Book("SGV Chuyen de Vat ly 10 CTST", "11216_20220623104147_wm_sgv-chuyen-de-hoc-tap-vat-li-10"),
]

for book in books:
    book.save()
