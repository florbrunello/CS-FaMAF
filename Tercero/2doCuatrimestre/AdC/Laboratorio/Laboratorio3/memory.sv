// Memory

module memory (input logic Branch_M, zero_M, 
					input logic InconBranch,
			   output logic PCSrc_M);

	assign PCSrc_M = (Branch_M & zero_M) | InconBranch;

endmodule

