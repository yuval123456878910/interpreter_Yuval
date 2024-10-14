set /p input= put the folder for setup: 
cd toRunTiME

cd setup
mkdir %input%\setup
cd setup
copy * %input%\setup 
cd ..
copy run.bat %input%
cd ..
