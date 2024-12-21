// Flopr TestBench

module flopr_tb();
	parameter N = 64;
	logic        clk, reset;
	logic        [N-1:0] d, q, qexpected;
	logic [100:0] i, errors;
	logic [128-1:0] testvectors [0:9] = '{  {64'b0000 , 64'b0000},
						{64'b0001 , 64'b0000},
						{64'b0010 , 64'b0000},
						{64'b0011 , 64'b0000},
						{64'b0100 , 64'b0000},
						{64'b0101 , 64'b0101},
						{64'b0110 , 64'b0110},
						{64'b0111 , 64'b0111},
						{64'b1000 , 64'b1000},
						{64'b1001 , 64'b1001}};

	// Instantiate device under test
	flopr #(N) dut(clk, reset, d, q);

	// Generate clock
	always     // no sensitivity list, so it always executes
		begin
			clk = 1; #5; clk = 0; #5;
		end
 
	// At start of test pulse reset
	initial 	
		begin     
			i = 0; errors = 0; {d, qexpected} = testvectors[0];
			reset = 1; qexpected = 'b0; #45; reset = 0;
		end

	// Apply test vectors on falling edge of clk
	always @(negedge clk)
		begin
			{d, qexpected} = testvectors[i];
		end	
	
	 
	// Check results on falling edge of clk
   	always @(posedge clk)
			begin
			#1;
			if (reset === '1) 
			begin
				if (qexpected !== 0) 
					begin
						$display("Error: qexpected !== '0");
						errors = errors + 1;
					end
			end

			if (reset === '0) 
				begin
				if (qexpected !== q) 
					begin
						$display("Error: qexpected !== q");
						errors = errors + 1;
					end
				end
				
			i = i + 1;
			
			if (testvectors[i] === 128'bx) 
				begin 
					$display("%d tests completed with %d errors", 
						 i, errors);
				//  $finish;
					$stop;
				end
			end

endmodule
