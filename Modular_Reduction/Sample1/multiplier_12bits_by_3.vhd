library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity multiplier_12bits_by_3 is
  port
  (
    clk  :  in std_logic;
    a_inv_b_floor  :  in unsigned (11 downto 0);
    b_a_inv_b_floor  :  out unsigned (11 downto 0)

  );
end multiplier_12bits_by_3;

architecture rtl of multiplier_12bits_by_3 is
constant b  :  unsigned (1 downto 0) := to_unsigned(3,2);


begin

process(clk)
begin
  if rising_edge(clk) then
    b_a_inv_b_floor <= a_inv_b_floor * b;
  end if;
end process;

end rtl;