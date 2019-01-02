from subprocess import call

#designed to process requests made from the main file, read the stored command in the bit.json, and call the appropriate c++ file.
bytc = json.loads(open('bit.json').read())
def read():
    #read the json file here.
    bytc_read = bytc['data']
    
if __name__ == '__main__':
    #main file
    #0 indicates first host, 1 is the command.
    if bytc_read = '01':
        call("./nrun/build/net_01.o")
    if bytc_read = '02':
        call("./nrun/build/net_01.o")
    if bytc_read = '03':
        call("./nrun/build/net_02.o")
    if bytc_read = '04':
        call("./nrun/build/net_03.o")
    if bytc_read = '05':
        call("./nrun/build/net_04.o")
    if bytc_read = '06':
        call("./nrun/build/net_05.o")
    if bytc_read = '07':
        call("./nrun/build/net_06.o")
    