cd D:\Users\edgar\Documents\GitHub\USAGE-LD
FOR /R "data\ZGZ\Residencial\Refined\" %%G IN (*.csv) DO (
    copy %%G data\ZGZ\Residencial\dataInProcess.csv

    echo [CONFIGURATION]>mapping\ZGZ\Residencial\configInProcess.ini
    echo output_file = data/ZGZ/Residencial/rdf/ZGZ-residencial-output-%%~nG-diagram.nq>>mapping\ZGZ\Residencial\configInProcess.ini
    echo number_of_processes=1 >>mapping\ZGZ\Residencial\configInProcess.ini
    echo output_format=N-QUADS >>mapping\ZGZ\Residencial\configInProcess.ini

    echo [DataSourceCSV]>>mapping\ZGZ\Residencial\configInProcess.ini
    echo mappings=mapping/ZGZ/Residencial/diagram/mappingZGZResidencial_diagram.ttl>>mapping\ZGZ\Residencial\configInProcess.ini
    echo file_path=data\ZGZ\Residencial\dataInProcess.csv>>mapping\ZGZ\Residencial\configInProcess.ini

    python -m morph_kgc mapping\ZGZ\Residencial\configInProcess.ini

    del mapping\ZGZ\Residencial\configInProcess.ini
    del data\ZGZ\Residencial\dataInProcess.csv
)