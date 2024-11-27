use anchor_lang::prelude::*;

declare_id!("FA4efgzBmfV5gudDvMb7AHMAKuPcuY1ZtfdJrxwjL8Q5");

#[program]
pub mod iot_data_storage {
    use super::*;

    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        msg!("Greetings from: {:?}", ctx.program_id);
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize {}
