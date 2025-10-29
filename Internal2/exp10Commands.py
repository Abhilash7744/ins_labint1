# 1️⃣ Check your network interface and IP address(just for this 172.20.8.0/22)
ip a

# 2️⃣ Update package lists
sudo apt update

# 3️⃣ Install Snort
sudo apt install snort -y

# 4️⃣ Edit Snort configuration file to set HOME_NET
sudo nano /etc/snort/snort.conf
# (Inside file → set)
 ipvar HOME_NET 172.20.8.0/22

# 5️⃣ Edit the local rules file to add a custom ICMP detection rule
sudo nano /etc/snort/rules/local.rules
# Add this rule at the end:
 alert icmp $HOME_NET any -> $EXTERNAL_NET any (msg:"IDS TEST: Outbound ICMP Ping Detected"; sid:1000001; rev:1;)

# 6️⃣ Test the Snort configuration for syntax errors
sudo snort -T -c /etc/snort/snort.conf

# 7️⃣ Run Snort in NIDS (Network IDS) mode on your interface (example: enp1s0)
sudo snort -A console -q -c /etc/snort/snort.conf -i enp1s0

# 8️⃣ In another terminal, generate ICMP traffic to trigger the rule
ping -c 1 8.8.8.8


