library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity multiplier_by_010101010101 is
  port
  (
    clk  :  in std_logic;
    a  :  in unsigned (11 downto 0);
    a_inv_b  :  out unsigned (11 downto 0)
  );
end multiplier_by_010101010101;

architecture rtl of multiplier_by_010101010101 is
  signal mult_result  :  unsigned (23 downto 0);


begin

mult_result <= a * "010101010101";
process(clk)
begin
  if rising_edge(clk) then
    a_inv_b <= mult_result(23 downto 12);
  end if;
end process;

end rtl;