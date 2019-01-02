/*
 * net_02.cpp
 *
 *  Created on: Dec 29, 2017
 *      Author: klaminite
 */
//Generates a few million sha256 key codes using random words, key code is private
#include "common.h"
using namespace std;

#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <openssl/bio.h>
#include <openssl/buffer.h>
#include <openssl/des.h>
#include <openssl/evp.h>
#include <openssl/pem.h>
#include <openssl/rsa.h>
#include <openssl/sha.h>
using namespace std;
string line;
string sha256(const string str)
{
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, str.c_str(), str.size());
    SHA256_Final(hash, &sha256);
    stringstream ss;
    for(int i = 0; i < SHA256_DIGEST_LENGTH; i++)
    {
        ss << hex << setw(2) << setfill('0') << (int)hash[i];
    }
    return ss.str();
}

int main(string x,string y)
{
	srand(time(0));
	srand (time(NULL));
   std::string input = "numbers.txt";
   std::ifstream infile( input.c_str( ) , std::ios::in ) ;
   std::string file( input ) ;
   std::getline( std::cin , input ) ;
	//iterate this over this so it does it in batches and not kill the ram
	//the more for statements added onto this code, the stronger the encryption key is, as long as the seed for each key is completely random, and meshes completely with the previous command.

	for (int i = 1; i <= 100; i++)
	{
		for (int i = 1; i <= 100; i++)
			{
				for (int i = 1; i <= 100; i++)
				    {
				       int linenumber = rand() % 400000 + 1;
				       int lines_read = 0 ;
				       std::string line ;
				       if ( infile.is_open( ) ) {
				          while ( infile ) {
				    	 getline( infile , line ) ;
				    	 lines_read++ ;

				    	    std::cout << sha256(line) << std::endl ;
				    	    break ;
							sleep(1);
				          }
				       }
				    }
			}
	}
}
