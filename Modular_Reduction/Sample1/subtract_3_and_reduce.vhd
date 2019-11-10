library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity subtract_3_and_reduce is
  port
  (
    clk  :  in std_logic;
    b_a_inv_b_floor  :  in unsigned (13 downto 0);
    a  :  in unsigned (11 downto 0);
    c  :  out unsigned (1 downto 0)

  );
end subtract_3_and_reduce;

architecture rtl of subtract_3_and_reduce is
signal sub_res  :  unsigned (2 downto 0);


begin

process(clk)
begin
  if rising_edge(clk) then
    sub_res <= a - b_a_inv_b_floor;
    if sub_res >= 3 then
      c <= sub_res - 3;
    else
      c <= sub_res - 0;
    end if;
  end if;
end process;

end rtl;