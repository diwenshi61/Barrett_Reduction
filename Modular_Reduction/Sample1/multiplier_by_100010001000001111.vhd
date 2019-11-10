library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity multiplier_by_100010001000001111 is
  port
  (
    clk  :  in std_logic;
    a  :  in unsigned (29 downto 0);
    a_inv_b  :  out unsigned (17 downto 0)
  );
end multiplier_by_100010001000001111;

architecture rtl of multiplier_by_100010001000001111 is
  signal mult_result  :  unsigned (47 downto 0);


begin

mult_result <= a * "100010001000001111";
process(clk)
begin
  if rising_edge(clk) then
    a_inv_b <= mult_result(47 downto 30);
  end if;
end process;

end rtl;