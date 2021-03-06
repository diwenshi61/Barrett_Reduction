library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity multiplier_17bits_by_7681 is
  port
  (
    clk  :  in std_logic;
    a_inv_b_floor  :  in unsigned (17 downto 0);
    b_a_inv_b_floor  :  out unsigned (29 downto 0)

  );
end multiplier_17bits_by_7681;

architecture rtl of multiplier_17bits_by_7681 is
constant b  :  unsigned (12 downto 0) := to_unsigned(7681,13);


begin

process(clk)
begin
  if rising_edge(clk) then
    b_a_inv_b_floor <= a_inv_b_floor * b;
  end if;
end process;

end rtl;