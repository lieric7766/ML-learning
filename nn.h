#ifndef NN_H
#define NN_H

class NN {
	public:
		NN();
		void network_grid();
		void load_model();
		void output_model(); 
		double predict();
		double accuracy();
		
	private:
		void train();
		double numerical_gradient();
		double gradient_descent();
};

#endif
