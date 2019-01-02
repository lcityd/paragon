#list of g++ commands for installing
g++ cypto.cpp -llibssh -lopenssl -o ./build/crypt.o
g++ libssh.cpp -llibssh -lopenssl -o ./build/libssh.o
g++ net.cpp -llibssh -lopenssl -o ./build/net.o
