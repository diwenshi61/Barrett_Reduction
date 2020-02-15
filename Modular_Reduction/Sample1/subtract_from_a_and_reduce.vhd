library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity subtract_from_a_and_reduce is
  port
  (
    clk  :  in std_logic;
    b_a_inv_b_floor  :  in unsigned (29 downto 0);
    a  :  in unsigned (29 downto 0);
    c  :  out unsigned (12 downto 0)

  );
end subtract_from_a_and_reduce;

architecture rtl of subtract_from_a_and_reduce is
signal sub_res  :  unsigned (13 downto 0);


begin

process(clk)
begin
  if rising_edge(clk) then
    sub_res <= a - b_a_inv_b_floor;
    if sub_res >= 7681 then
      c <= sub_res - 7681;
    else
      c <= sub_res - 0;
    end if;
  end if;
end process;

end rtl;