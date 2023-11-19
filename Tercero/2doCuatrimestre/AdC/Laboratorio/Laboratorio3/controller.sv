// Controller

module controller (input logic reset, 
						 input logic [10:0] instr,
						 input logic ExcAck,
						 input logic ExtIRQ, 
						 output logic [3:0] AluControl,
						 output logic reg2loc, regWrite, 
						 output logic [1:0] AluSrc,
						 output logic Branch, memtoReg, memRead, memWrite,				 
						 output logic Exc, ERet, 
					    output logic [3:0] EStatus, 
						 output logic ExtIAck, 
						 output logic InconBranch);

	logic [1:0] AluOp_s;
	
	maindec 	decPpal (.Op(instr), 
							.reset(reset),
							.Reg2Loc(reg2loc), 
							.ALUSrc(AluSrc), 
							.MemtoReg(memtoReg), 
							.RegWrite(regWrite), 
							.MemRead(memRead), 
							.MemWrite(memWrite), 
							.Branch(Branch), 
							.ALUOp(AluOp_s),
							.ERet(ERet), 							
							.NotAnInstr(NotAnInstr), 
							.InconBranch(InconBranch));						
							
	aludec 	decAlu 	(.funct(instr), 
							.aluop(AluOp_s), 
							.alucontrol(AluControl));

	always_comb
		begin
			if (reset) 									// reset == 1, todas las salidas de controller valen 0 
				begin 
					EStatus <= 4'b0000;
					Exc <= 1'b0000;			
					ExtIAck <= 1'b0000;	
				end
			
			else 									     // reset == 0
				begin 
					begin 
						if (ExtIRQ) 
							EStatus <= 4'b0001; 
						else if (NotAnInstr) 
							EStatus <= 4'b0010; 
						else
							EStatus <= 4'b0000;
					end 
					Exc <= (ExtIRQ | NotAnInstr);			
					ExtIAck <= (ExcAck & ExtIRQ) ? 1'b1 : 1'b0; 
				end
		end
		
endmodule
