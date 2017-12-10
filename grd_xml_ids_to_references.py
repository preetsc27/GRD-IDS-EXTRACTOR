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

# scanning the directory for all the files
path = "."
allFiles = os.listdir(path)
files_list = []
for file in allFiles:
    filePath = os.path.join(path, file)
    if os.path.isfile(filePath):
        if file.startswith("."):
            continue
        files_list.append(file)

# showing the files

if len(files_list) == 0: # empty check
    print("No files found to show")
    sys.exit()
else:
    file_i = 1
    for file in files_list:
        print(file_i, file)
        file_i += 1

chosen_file_number = int(input("Enter the file number from the list above:"))
xml_file = files_list[chosen_file_number - 1]

choose_lang = int(input("Choose language:\n1.Kotlin\n2.Java\n"))

if choose_lang >  2 or choose_lang < 1:
    print(bcolors.FAIL + "Choose 1 or 2 for language." + bcolors.ENDC)
elif (os.path.exists(xml_file) == False):
    print( bcolors.FAIL + "The file {} does not exsits.".format(xml_file) + bcolors.ENDC)
else:
    with open(xml_file) as fp:
        line =  fp.readline()
        cnt = 1
        view = None

        # lists of vies and ids
        views_list = []
        ids_list = []

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

                    # adding data to the lists
                    views_list.append(view)
                    ids_list.append(got_id)

                    # incrementing the count var
                    cnt += 1
            line = fp.readline()

        # priniting the data (direct reference)
        print(bcolors.OKBLUE + "Direct".format(xml_file) + bcolors.ENDC)
        for i in range (0, len(views_list)):

            # getting the individual values from list
            view = views_list[i]
            got_id = ids_list[i]

            # selected language check
            if choose_lang == 1:
                print("val {} = findViewById<{}>(R.id.{})".format(got_id, view, got_id))

                # Ignore for now
                got_id_got = "got"+got_id.capitalize()
                out = """
                val {} = {}.text.toString().trim()
                if({}.isEmpty()){}
                    Misc().myT(this, "Please enter {}.", 0)
                    return@setOnClickListener
                {}""".format(got_id_got, got_id, got_id_got, "{", got_id.capitalize(), "}")
                #print(out)
            elif choose_lang == 2:
                print("{} {} = ({}) findViewById(R.id.{});".format(view, got_id, view, got_id))
        
        # priniting the data (variables declaration)
        print("")
        print(bcolors.OKGREEN + "InDirect Part-1".format(xml_file) + bcolors.ENDC)
        for i in range (0, len(views_list)):

            # getting the individual values from list
            view = views_list[i]
            got_id = ids_list[i]

            # selected language check
            if choose_lang == 1:
                print("private var {}: {}? = null".format(got_id, view))
            elif choose_lang == 2:
                print("private {} {};".format(view, got_id))

        # priniting the data (declared variables initialisation)
        print("")
        print(bcolors.OKGREEN + "InDirect Part-2".format(xml_file) + bcolors.ENDC)
        for i in range (0, len(views_list)):

            # getting the individual values from list
            # view = views_list[i]. No need of view.
            got_id = ids_list[i]

            # selected language check
            if choose_lang == 1:
                print("{} = findViewById(R.id.{})".format(got_id, got_id))
            elif choose_lang == 2:
                print("{} = ({}) findViewById(R.id.{});".format(got_id, view, got_id))

        # priniting the data (buttons set on click listener)
        print("")
        print(bcolors.HEADER + "Set On Click Listeners for Buttons".format(xml_file) + bcolors.ENDC)
        for i in range (0, len(views_list)):

            # getting the individual values from list
            view = views_list[i]
            got_id = ids_list[i]

            # button check
            if view == "Button":
                # selected language check
                if choose_lang == 1:
                    print("{}.setOnClickListener {} {}".format(got_id, "{", "}"))
                elif choose_lang == 2:
                    print("{}.setOnClickListener(new View.OnClickListener() {} {});".format(got_id, "{", "}"))

    print("\nToatl {} ids found.".format(cnt))
        