// Execute

module execute (input logic AluSrc, 
					 input logic [3:0] AluControl, 
					 input logic [63:0] PC_E, signImm_E, readData1_E, readData2_E, 
					 output logic [63:0] PCBranch_E, aluResult_E, writeData_E, 
					 output logic zero_E); 

	logic [63:0] mux2_output, sl2_output; 
	
	mux2 MUX(readData2_E, signImm_E, AluSrc, mux2_output); 
	sl2 ShiftLeft2(signImm_E, sl2_output);
	adder Add(PC_E, sl2_output, PCBranch_E); 
	alu ALU(readData1_E, mux2_output, AluControl, aluResult_E, zero_E); 

	assign writeData_E = readData2_E;
	
endmodule

				