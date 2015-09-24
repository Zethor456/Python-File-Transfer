/*
 * main.cxx
 * 
 * Copyright 2015 Tom Fraser <tfraser1@vmicron01>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */

#include <fstream>
#include <stdio.h>
#include <iostream>
#include <unistd.h>
#define GetCurrentDir getcwd 
using namespace std;



int ls(string path){
	fprintf( stdout, "%s", path.c_str() );
	string comand("ls " + path);
	
	FILE * f = popen( comand.c_str(),"r");
	if (f==0) {
		fprintf(stderr, "Could not execute\n");
		return -1;
	}
	const int BUFSIZE = 1000;
	char buf[ BUFSIZE ];
	while ( fgets(buf, BUFSIZE, f ) ) {
		fprintf( stdout, "%s", buf );
	}
	pclose( f ); 
	return 0;
}

string cd(string fromClient, string path){
	string comand("cd "+ path + " ; " + fromClient + "; pwd ");
	
	fprintf(stdout, "%s \n", comand.c_str());
	FILE * f = popen( comand.c_str(),"r");
	if (f==0) {
		fprintf(stderr, "Could not execute\n");
		return "failed";
	}
	const int BUFSIZE = 1000;
	char buf[ BUFSIZE ];
	while ( fgets(buf, BUFSIZE, f ) ) {
		string newpath(buf);
		fprintf( stdout, "%s", buf );
	}
	pclose( f ); 
	
	return buf;
}


int main(int argc, char **argv)
{
	
	char cCurrentPath[FILENAME_MAX];

 GetCurrentDir(cCurrentPath, sizeof(cCurrentPath));
	string path(cCurrentPath);
 /*cCurrentPath[sizeof(cCurrentPath) - 1] = '\0';  not really required */
 //printf ("The current working directory is %s", cCurrentPath);
	
	/*ofstream myfile;
	myfile.open("/home/4user1/tfraser1/example.txt");
	myfile << "Writing this to a file/n";
	myfile.close();*/
	//FILE * f = popen( "ls  /home/4user1/tfraser1/","r");
	/*FILE * f = popen( "pwd ","r");
	if (f==0) {
		fprintf(stderr, "Could not execute\n");
		return 1;
	}
	const int BUFSIZE = 1000;
	char buf[ BUFSIZE ];
	while ( fgets(buf, BUFSIZE, f ) ) {
		fprintf( stdout, "%s", buf );
	}
	pclose( f );*/
	
	//ls(path);
	string test("cd ..");
	cd(test,path);
	
	
	
	return 0;
	
	
	
}
