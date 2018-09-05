#include <iostream>
#include <vector>
#include <string>

#include "nn.h"


NN::NN()
{}

void NN::network_grid(std::vector<int> v, std::string activate) {
	std::vector<std::vector<std::vector<int> > > all_weight_grids;
	for (std::vector<int>::iterator iter = v.begin(); iter != v.end(); ++iter) {
		std::vector<std::vector<int> > weight_grid(v[iter], std::vector<int>(v[iter]+1));
		all_weight_grids.push_back(weight_grid); 
	}	

}

void NN::load_model() {
	//
}

void NN::output_model() {
	//
}

double NN::predict() {
	//
}

double NN::accuracy() {
	//
}

