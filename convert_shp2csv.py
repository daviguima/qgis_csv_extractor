from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterVectorLayer
from qgis.core import QgsProcessingParameterVectorDestination
import processing


class Extract_shapetable_to_csv(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer('vetorentrada', 'vetor_entrada', types=[QgsProcessing.TypeVectorPoint], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorDestination('Saidacsv', 'saida.csv', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(1, model_feedback)
        results = {}
        outputs = {}

        # Convert format
        alg_params = {
            'INPUT': parameters['vetorentrada'],
            'OPTIONS': '',
            'OUTPUT': parameters['Saidacsv']
        }
        outputs['ConvertFormat'] = processing.run('gdal:convertformat', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Saidacsv'] = outputs['ConvertFormat']['OUTPUT']
        return results

    def name(self):
        return 'extract_shapeTable_to_csv'

    def displayName(self):
        return 'extract_shapeTable_to_csv'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Extract_shapetable_to_csv()
