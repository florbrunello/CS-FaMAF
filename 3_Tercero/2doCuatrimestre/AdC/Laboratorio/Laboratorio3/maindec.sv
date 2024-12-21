// Maindec

module maindec (input logic [10:0] Op,
					 input logic reset,
					 output logic Reg2Loc, 
					 output logic [1:0] ALUSrc, 
					 output logic MemtoReg, RegWrite, MemRead, MemWrite, Branch, 
					 output logic [1:0] ALUOp, 
					 output logic ERet, 					 
					 output logic NotAnInstr, 
					 output logic InconBranch); 	
		
	always_comb
		begin 
			if (reset == 1)	// Si reset == 1, todas las salidas de controller valen 0 
				begin 
					Reg2Loc <= 1'b0;
					ALUSrc <= 2'b0;
					MemtoReg <= 1'b0;
					RegWrite <= 1'b0;
					MemRead <= 1'b0;
					MemWrite <= 1'b0;
					Branch <= 1'b0;
					ALUOp <= 2'b00;
					ERet <= 1'b0; 
					NotAnInstr <= 1'b0; 
					InconBranch <= 1'b0; 					
				end
			
			else begin // reset == 0
				casez(Op)

					11'b101_0101_0000: //R-type
					begin
						Reg2Loc <= 1'b0;
						ALUSrc <= 2'b00;
						MemtoReg <= 1'b0;
						RegWrite <= 1'b1;
						MemRead <= 1'b0;
						MemWrite <= 1'b0;
						Branch <= 1'b0;
						ALUOp <= 2'b10;
						ERet <= 1'b0; 
						NotAnInstr <= 1'b0; 
						InconBranch <= 1'b0; 						
					end
					
					11'b111_1100_0010: //LDUR
					begin
						Reg2Loc <= 1'b?;
						ALUSrc <= 2'b01;
						MemtoReg <= 1'b1;
						RegWrite <= 1'b1;
						MemRead <= 1'b1;
						MemWrite <= 1'b0;
						Branch <= 1'b0;
						ALUOp <= 2'b00;
						ERet <= 1'b0; 
						NotAnInstr <= 1'b0; 
						InconBranch <= 1'b0; 						
					end

					11'b111_1100_0000: //STUR
					begin
						Reg2Loc <= 1'b1;
						ALUSrc <= 2'b01;
						MemtoReg <= 1'b?;
						RegWrite <= 1'b0;
						MemRead <= 1'b0;
						MemWrite <= 1'b1;
						Branch <= 1'b0;
						ALUOp <= 2'b00;
						ERet <= 1'b0; 				
						NotAnInstr <= 1'b0; 
						InconBranch <= 1'b0; 						
					end

					11'b101_1010_0???: // CBZ
					begin
						Reg2Loc <= 1'b1;
						ALUSrc <= 2'b00;
						MemtoReg <= 1'b?;
						RegWrite <= 1'b0;
						MemRead <= 1'b0;
						MemWrite <= 1'b0;
						Branch <= 1'b1;
						ALUOp <= 2'b01;
						ERet <= 1'b0;				
						NotAnInstr <= 1'b0; 
						InconBranch <= 1'b0; 						
					end

					11'b110_1011_0100: // ERET
					begin
						Reg2Loc <= 1'b0;
						ALUSrc <= 2'b00;
						MemtoReg <= 1'b?;
						RegWrite <= 1'b0;
						MemRead <= 1'b0;
						MemWrite <= 1'b0;
						Branch <= 1'b1;
						ALUOp <= 2'b01;
						ERet <= 1'b1;				
						NotAnInstr <= 1'b0; 
						InconBranch <= 1'b0; 						
					end

					11'b?11_0101_0100: // MRS
					begin
						Reg2Loc <= 1'b1;
						ALUSrc <= 2'b1?;
						MemtoReg <= 1'b0;
						RegWrite <= 1'b1;
						MemRead <= 1'b0;
						MemWrite <= 1'b0;
						Branch <= 1'b0;
						ALUOp <= 2'b01;
						ERet <= 1'b0;
						NotAnInstr <= 1'b0;
						InconBranch <= 1'b0; 						
					end
					
					11'b110_1011_0000: // BR
					begin
						Reg2Loc <= 1'b0;
						ALUSrc <= 2'b00;
						MemtoReg <= 1'b0;
						RegWrite <= 1'b1;
						MemRead <= 1'b0;
						MemWrite <= 1'b0;
						Branch <= 1'b0;
						ALUOp <= 2'b01;
						ERet <= 1'b0; 
						NotAnInstr <= 1'b0; 
						InconBranch <= 1'b1; 
					end
					

					default: //InvalidOpCode
					begin
						Reg2Loc <= 1'b?;
						ALUSrc <= 2'b??;
						MemtoReg <= 1'b0;
						RegWrite <= 1'b0;
						MemRead <= 1'b0;
						MemWrite <= 1'b0;
						Branch <= 1'b0;
						ALUOp <= 2'b??;
						ERet <= 1'b0; 
						NotAnInstr <= 1'b1; 
						InconBranch <= 1'b0; 
					end
				endcase
		end
	end

endmodule

