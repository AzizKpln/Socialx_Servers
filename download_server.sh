while :
do
 
    for a in $(ssh -i 'mm.pem' ubuntu@server.amazonaws.com ls -l  /var/www/html/images | awk '{print $9}')
        do
            if [ -f $a ]
                then
                    true
            else
                scp -i "mm.pem" ubuntu@eserver.amazonaws.com:/var/www/html/images/* . 
           fi
        done
    unzip \*.hta.zip
    sudo cp -r * /var/www/html/
    sudo rm /var/www/html/mm.pem
    sudo rm /var/www/html/bot.sh

done
