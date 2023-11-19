module signext_tb3();
	logic [31:0] a; 
	logic [63:0] y;
	
	// Instantiate device under test
	signext dut(a, y);
	
	always begin 
			a = {11'b111_1100_0010, 9'b0_1110_0011, 2'b00, 5'b01001, 5'b10110};
			#10;
			if (y !== {55'b0, 9'b0_1110_0011}) 
				$display("Error: yexpected !== y");
				
			a = {11'b111_1100_0010, 9'b0_1110_0011, 2'b00, 5'b01001, 5'b10110};
			#10;
			if (y !== {55'b1, 9'b0_1110_0011}) 
				$display("Error: yexpected !== y");

			a = {11'b111_1100_0010, 9'b0_1110_0011, 2'b00, 5'b01001, 5'b10110};
			#10;
			if (y !== {55'b0, 9'b0_1110_0011}) 
				$display("Error: yexpected !== y");

			a = {11'b111_1100_0010, 9'b0_1110_0011, 2'b00, 5'b01001, 5'b10110};
			#10;
			if (y !== {55'b1, 9'b0_1110_0011}) 
				$display("Error: yexpected !== y");

			a = {8'b1011_0100, 19'b001_1110_0011_1111_1010, 5'b10110};
			#10;
			if (y !== {45'b0, 19'b001_1110_0011_1111_1010}) 
				$display("Error: yexpected !== y");

			a = {8'b1011_0100, 19'b101_1110_0011_1111_1010, 5'b10110};
			#10;
			if (y !== {45'b1, 19'b101_1110_0011_1111_1010})  
				$display("Error: yexpected !== y");

			a = {11'b100_0101_1000, 5'b10101, 6'b000000, 5'b10100, 5'b01001};
			#10;
			if (y !== 64'b0) 
				$display("Error: yexpected !== y");			
			$stop;
		end 			
endmodule
			
