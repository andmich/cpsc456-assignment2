#include <string>
#include "codearray.h"
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <vector>
#include <sys/stat.h>
#include <sys/types.h>

using namespace std;

int main()
{

	/* The child process id */
	pid_t childProcId = -1;

	/* Go through the binaries */
	for(int progCount = 0; 	progCount < NUM_BINARIES; ++progCount)
	{

		// Create a temporary file you can use the tmpnam() function for this.
		char* fileName = tmpnam(NULL);

		// Open the file and write the bytes of the first program to the file.
		FILE* fp = fopen(fileName, "wb");

		if(!fp)
		{
			perror("fopen");
			exit(-1);
		}

		if(fwrite(codeArray[progCount], sizeof(char), programLengths[progCount], fp) < 0)
		{
			perror("fwrite");
			exit(-1);
		}
		fclose(fp);

		// Make the file executable.
		chmod(fileName, 0777);

		// Create a child process using fork
		childProcId = fork();

		if (childProcId < 0) { /* error occurred */
			fprintf(stderr, "Fork Failed");
			exit(-1);
		}
		/* I am a child process; I will turn into an executable */
		if(childProcId == 0)
		{
			if(execlp(fileName, fileName, NULL) < 0) {
				perror("execlp");
				exit(-1);
			}
		}
	}

	/* Wait for all programs to finish */
	for(int progCount = 0; progCount < NUM_BINARIES; ++progCount)
	{
		/* Wait for one of the programs to finish */
		if(wait(NULL) < 0)
		{
			perror("wait");
			exit(-1);
		}
	}
}
