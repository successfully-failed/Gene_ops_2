#include <iostream>
#include <vector>
#include <string>


//support functions
std::string string_checker(std::string string, 
			   int option/* to choose between checking DNA and RNA*/);
std::string string_returner(std::string string);
std::vector<std::string> codon_finder(std::string refactored_string);

//"workhorse" functions
std::string replicator(std::string refactored_string);
std::string transcriptor(std::string refactored_string);
std::string translator(std::vector<std::string> codons);

//"main functions
std::string replication(std::string DNA_string, int opt_a)
{

	std::string temp_string = DNA_string;
	//this exists to connect eventual strings into one output
	std::string final_string;
	if(opt_a == 1)
	{
		final_string = string_returner(temp_string);
	}
	//Adds a result into the final string
	final_string = final_string + replicator(string_checker(temp_string, 0));
	return final_string;
}

std::string transcription (std::string DNA_string, int opt_a)
{
	std::string temp_string = DNA_string;
	std::string final_string;
	if(opt_a == 1)
	{
		final_string = string_returner(temp_string);
	}
	final_string = final_string + transcriptor(string_checker(temp_string, 0));
	return final_string;
}


std::string translation(std::string DNA_string, int opt_a, int opt_b, int opt_c)
{
	std::string temp_string = DNA_string;
	std::string final_string;
	if(opt_a == 1)
	{
		final_string = string_returner(temp_string);
	}
	if(opt_b == 1)
	{
	    	std::vector<std::string> temp_vector;
		std::string codon_string;
		//if dna string was given
		if(opt_c == 1)
		{
	 	   	temp_vector = 
				codon_finder(
					transcriptor(
					    string_checker(temp_string, 0)));
		}
		else
		{
			temp_vector = 
				codon_finder(
					string_checker(temp_string, 1));
		}
		for(int i = 0; i <= temp_vector.size(); i++)
      		{
			codon_string += temp_vector[i];
		}
		codon_string += "\n\n";
		final_string += codon_string;
	}
	if(opt_c == 1)
	{
		final_string += translator(
				codon_finder(
				string_checker(temp_string, 1)));
	}
	else 
	{
		final_string += translator(
				codon_finder(
				transcriptor(
				string_checker(temp_string, 0))));
	}
	return final_string;
}
int main()
{
return 0;
}

