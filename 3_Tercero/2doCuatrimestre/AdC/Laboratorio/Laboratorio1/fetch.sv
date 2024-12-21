// Fetch 

module fetch (input logic PCSrc_F, clk, reset, 
				  input logic [63:0] PCBranch_F, 
				  output logic [63:0] imem_addr_F); 

	logic [63:0] mux2_output, adder_output;
	logic [63:0] adder_input = 64'd4;
	
	mux2 MUX(adder_output, PCBranch_F, PCSrc_F, mux2_output); 
	flopr PC(clk, reset, mux2_output, imem_addr_F);
	adder Add(imem_addr_F, adder_input, adder_output);

endmodule