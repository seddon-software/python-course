clear
fuser -k 7000/tcp
createProject.sh
sleep 10
createWebApp.sh
sleep 10
run
sleep 10
modifySettings.sh
sleep 10
migrate.sh
sleep 10
generateModels.sh
sleep 10
createView.sh
sleep 10
createUrls.sh
sleep 10
doShell.sh
sleep 10
firefox http://localhost:7000/salaries

