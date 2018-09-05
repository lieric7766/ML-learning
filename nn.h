#ifndef NN_H
#define NN_H

#include <vector>
#include <string>

class NN {
	public:
		NN();
		void network_grid(std::vector<int>, std::string);
		void load_model();
		void output_model(); 
		double predict();
		double accuracy();
		
	private:
		void train();
		double numerical_gradient();
		double gradient_descent();
		double sigmoid();
		double relu();
};

#endif
