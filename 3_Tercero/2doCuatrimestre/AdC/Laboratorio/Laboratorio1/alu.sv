// Alu

module alu (input logic [63:0] a, b,
				input logic [3:0] ALUControl, 
				output logic [63:0] result, 
				output logic zero);

	always_comb 
		begin
			
			zero = 0; 
			
			case(ALUControl) 
				4'b0000: result = a & b;
				4'b0001: result = a | b;
				4'b0010: result = a + b;
				4'b0110: result = a - b;
				4'b0111: result = b;
				
				default: result = 64'b1;
			endcase					
			
			if (result == 0) begin 
				zero = 1;
			end

		end
endmodule