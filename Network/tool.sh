



read -p "ip/hostname: " ip
echo "Which tool do you want to use Cosmos?"
echo "1 - Anubis: Subdomain Finder"
echo "2 - ipinfo: IP Informtion Gathering"
echo "3 - Nmap: Port Scanning"
read input;
echo "Tool Number: $input for $ip"

case $input in
            1) anubis -t $ip;;
            2) ipinfo $ip;;
            3) nmap $ip;;

esac