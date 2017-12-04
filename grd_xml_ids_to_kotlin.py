import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

intro = bcolors.HEADER +  """

                        GRD IDS EXTRACTOR

HELLO IT IS AN OPEN SOURCE SOFTWARE TO CONVERT ALL THE IDS IN XML FILE TO CREATE THE REFERENCE IN ON IT IN THE ACTIVITY FILE.

IT SUPPORTS BOTH JAVA AND KOTLIN.
""" + bcolors.ENDC + bcolors.WARNING + "\nNOTE: RUN IT IN XML FILE DIRECTORY." +bcolors.ENDC


print(intro)
choose_lang = int(input("Choose language:\n1.Kotlin\n2.Java\n"))
xml_file = input("Enter XML file name: ")
if choose_lang >  2 or choose_lang < 1:
    print(bcolors.FAIL + "Choose 1 or 2 for language." + bcolors.ENDC)
elif (os.path.exists(xml_file) == False):
    print( bcolors.FAIL + "The file {} does not exsits.".format(xml_file) + bcolors.ENDC)
else:
    with open(xml_file) as fp:
        line =  fp.readline()
        cnt = 1
        view = None
        while line:
            # cuuting down the spaces
            trim_line = line.strip()
            # checking if there is something on this line or not
            if len(trim_line) > 1:
                # looking for the new tag opening
                if trim_line[0] == '<':
                    #stripping down the '<' symbol
                    view = trim_line.strip('<')
                
                # looking for id tag
                if "android:id" in trim_line:
                    # splitting the line into list
                    line_list = trim_line.split('/')

                    # stripping the " from it
                    got_id = line_list[1].strip('"')

                    # selected language check
                    if choose_lang == 1:
                        print("val {} = findViewById<{}>(R.id.{})".format(got_id, view, got_id))
                    elif choose_lang == 2:
                        print("{} {} = ({}) findViewById(R.id.{}); ".format(view, got_id, view, got_id))
                    # incrementing the count var
                    cnt += 1
            line = fp.readline()
    print("Toatl {} ids found.".format(cnt))
        
