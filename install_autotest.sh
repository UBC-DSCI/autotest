if ! type nbgrader
then
    echo "nbgrader-0.6.2 or higher was not installed"
fi

nbgrader_path=$(pip show nbgrader | grep "^Location:*" | cut -c11-)
echo $nbgrader_path

cp converters/generate_assignment.py $nbgrader_path/nbgrader/converters
cp preprocessors/instantiatetests.py $nbgrader_path/nbgrader/preprocessors
cp preprocessors/limittestcellheights.py $nbgrader_path/nbgrader/preprocessors
cp preprocessors/__init__.py $nbgrader_path/nbgrader/preprocessors
cp preprocessors/execute.py $nbgrader_path/nbgrader/preprocessors

cp -r nbextensions/limit_cell_height $nbgrader_path/nbgrader/nbextensions
cp __init__.py $nbgrader_path/nbgrader


echo "installing nbgrader extensions"
jupyter nbextension install --sys-prefix --py nbgrader --overwrite
jupyter nbextension enable --sys-prefix --py nbgrader
jupyter serverextension enable --sys-prefix --py nbgrader
