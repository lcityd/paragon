#include "common.h"
//============================================================================
// Name        : net.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Main Controller for stack processes
//============================================================================

#define LIBSSH_STATIC 1
#define server
//INCLUDES
#include <common.h>
//PROGRAM
const void* test;

//json extraction here; takes commands and command parameters

//if you made it past that ur not toasted
void menu() {
	std::string x;
	std::string cmd;
	std::cout << "[Server] Hello, Welcome to Paragon Servers, copyright vontech 2017\n[Server] Choose a command";
	std::cin >> x;
	if (x == "start"){
			std::cout << "[Server] Welcome!";
			std::system("/PARAGON/BOOT/SystemBoot.py"); //start up this file after the cryptocheck
	}
	//all the same IP until Wednesday
	if (x == "server_1"){
		server_main("klaminite@192.168.1.3");
			if (cmd == "reboot");
				x = cmd;
	}
	if (x == "server_2"){
		server_main("klaminite@192.168.1.3");
		if (cmd == "reboot");
			x = cmd;
	}
	if (x == "server_3"){
		server_main("klaminite@192.168.1.3");
		if (cmd == "reboot");
			x = cmd;
	}
	if (x == "server_4"){
		server_main("klaminite@192.168.1.3");
		if (cmd == "reboot");
			x = cmd;
	}
};
void norm() {

};
int main(){
	//here lies all the class calls
	runcheck();
}

//do something herre