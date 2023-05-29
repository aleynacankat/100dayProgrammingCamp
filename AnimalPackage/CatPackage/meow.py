def speak_direct():
    print("meow direct")

def speak2_imported():
    print("meow imported")

if __name__== "__maindeme__":
    speak_direct()
else:
    speak2_imported()