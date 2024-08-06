
from rest_framework.views import APIView
from rest_framework import serializers, routers, viewsets, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.db.models import Q


from .models import ModeloEvaluacion,CriterioEvaluacion, SubCriterioEvaluacion
from .models import TipoIndicador,IndicadorEvaluacion,EvidenciaEvaluacion
from .models import PeriodoAcademico, DocumentoEvaluacion

from .serializers import criteriosEvaluacion_Serializer, documentosEvaluacion_Serializer, periodoAcademico_Serializer


class Evaluacion_evidencia(APIView):
    def get(self, request):
        data = []
        modelos = ModeloEvaluacion.objects.all()
        for modelo_i in modelos:
            criterios = CriterioEvaluacion.objects.filter(modeloEvaluacion=modelo_i)
            for criterio_i in criterios:
                subcriterios = SubCriterioEvaluacion.objects.filter(criterioEvaluacion=criterio_i)
                for subcriterio_i in subcriterios:
                    indicadores = IndicadorEvaluacion.objects.filter(subCriterioEvaluacion=subcriterio_i)
                    for indicador_i in indicadores:
                        evidencias = EvidenciaEvaluacion.objects.filter(indicadorEvaluacion=indicador_i).order_by('numeral')
                        for evidencia_i in evidencias:
                            data.append({
                                'modelo':modelo_i.nombre,
                                'criterio':criterio_i.nombre,
                                'subcriterio':subcriterio_i.nombre,
                                'indicador_numeral':indicador_i.numeral,
                                'indicador':indicador_i.nombre,
                                'evidencia_numeral': evidencia_i.numeral,
                                'evidencia':evidencia_i.nombre,
                                'evidenciaID':evidencia_i.id,
                            })
        data2 = []
        for datos in data:
            documentos = DocumentoEvaluacion.objects.filter(evidenciaEvaluacion=datos['evidenciaID']).order_by('numeral')
            if not documentos:
                
                data2.append({
                    'modelo':datos['modelo'],
                    'criterio':datos['criterio'],
                    'subcriterio':datos['subcriterio'],
                    'indicador_numeral':datos['indicador_numeral'],
                    'indicador':datos['indicador'],
                    #'evidencia_numeral': evidencia_i.numeral,
                    'evidencia':datos['evidencia'],
                    #'evidenciaID':evidencia_i.id,
                                   
                })
            for documentos_i in documentos:
                #datos['documento'] = documentos_i.nombre
                data2.append({
                    'modelo':datos['modelo'],
                    'criterio':datos['criterio'],
                    'subcriterio':datos['subcriterio'],
                    'indicador_numeral':datos['indicador_numeral'],
                    'indicador':datos['indicador'],
                    #'evidencia_numeral': evidencia_i.numeral,
                    'evidencia':datos['evidencia'],
                    #'evidenciaID':evidencia_i.id,
                    'documento':documentos_i.nombre,                  
                })
                
            
        return Response(data2)
    
    
class Evaluacion_evidencia_fil_ModeloCriterio(APIView):
    def get(self, request):
        data = []
        criterio_id = request.query_params.get('criterio_id', None)
        #print('criterio',criterio_id)

        #if modelo_id is not None:
        #    modelos = ModeloEvaluacion.objects.filter(id=modelo_id)
        #else:
        #    modelos = ModeloEvaluacion.objects.all()
        
        modelos = ModeloEvaluacion.objects.all()
        for modelo_i in modelos:
            criterios = CriterioEvaluacion.objects.filter(id=criterio_id)
            for criterio_i in criterios:
                subcriterios = SubCriterioEvaluacion.objects.filter(criterioEvaluacion=criterio_i)
                for subcriterio_i in subcriterios:
                    indicadores = IndicadorEvaluacion.objects.filter(subCriterioEvaluacion=subcriterio_i)
                    for indicador_i in indicadores:
                        evidencias = EvidenciaEvaluacion.objects.filter(indicadorEvaluacion=indicador_i).order_by('numeral')
                        for evidencia_i in evidencias:
                            responsable = indicador_i.responsable
                            responsable_id = responsable.id if responsable else None
                            responsable_nombre = f"{responsable.first_name} {responsable.last_name}" if responsable else "Sin responsable"
                            
                            corresponsable1 = indicador_i.coresponsable1
                            corresponsable1_id = corresponsable1.id if corresponsable1 else None
                            corresponsable1_nombre = f"{corresponsable1.first_name} {corresponsable1.last_name}" if corresponsable1 else ""
                            
                            corresponsable2 = indicador_i.coresponsable2
                            corresponsable2_id = corresponsable2.id if corresponsable2 else None
                            corresponsable2_nombre = f"{corresponsable2.first_name} {corresponsable2.last_name}" if corresponsable2 else ""
                            
                            corresponsable3 = indicador_i.coresponsable3
                            corresponsable3_id = corresponsable3.id if corresponsable3 else None
                            corresponsable3_nombre = f"{corresponsable3.first_name} {corresponsable3.last_name}" if corresponsable3 else ""
                            
                            corresponsable4 = indicador_i.coresponsable4
                            corresponsable4_id = corresponsable4.id if corresponsable4 else None
                            corresponsable4_nombre = f"{corresponsable4.first_name} {corresponsable4.last_name}" if corresponsable4 else ""
                        
                            corresponsable5 = indicador_i.coresponsable5
                            corresponsable5_id = corresponsable5.id if corresponsable5 else None
                            corresponsable5_nombre = f"{corresponsable5.first_name} {corresponsable5.last_name}" if corresponsable5 else ""
                            
                            data.append({
                                'modelo':modelo_i.nombre,
                                'criterio':criterio_i.nombre,
                                'subcriterio':subcriterio_i.nombre,
                                'indicador_numeral':indicador_i.numeral,
                                'indicador':indicador_i.nombre,
                                'responsableIndicadorID':responsable_id,
                                'responsableIndicador': responsable_nombre,
                                'corresponsableIndicador1ID':corresponsable1_id,
                                'corresponsableIndicador1':corresponsable1_nombre,
                                
                                'corresponsableIndicador2ID':corresponsable2_id,
                                'corresponsableIndicador2':corresponsable2_nombre,
                                
                                'corresponsableIndicador3ID':corresponsable3_id,
                                'corresponsableIndicador3':corresponsable3_nombre,
                                
                                'corresponsableIndicador4ID':corresponsable4_id,
                                'corresponsableIndicador4':corresponsable4_nombre,
                                'corresponsableIndicador5ID':corresponsable5_id,
                                'corresponsableIndicador5':corresponsable5_nombre,
                               
                                'evidencia_numeral': evidencia_i.numeral,
                                'evidencia':evidencia_i.nombre,
                                'evidenciaID':evidencia_i.id,
                                
                                
                            })
        data2 = []
        for datos in data:
            documentos = DocumentoEvaluacion.objects.filter(evidenciaEvaluacion=datos['evidenciaID']).order_by('numeral')
            if not documentos:
                
                data2.append({
                    'modelo':datos['modelo'],
                    'criterio':datos['criterio'],
                    'subcriterio':datos['subcriterio'],
                    'indicador_numeral':datos['indicador_numeral'],
                    'indicador':datos['indicador'],
                    'responsableIndicadorID':datos['responsableIndicadorID'],
                    'responsableIndicador': datos['responsableIndicador'],
                    'corresponsableIndicador1ID':datos['corresponsableIndicador1ID'],
                    'corresponsableIndicador1':datos['corresponsableIndicador1'],
                    'corresponsableIndicador2ID':datos['corresponsableIndicador2ID'],
                    'corresponsableIndicador2':datos['corresponsableIndicador2'],
                    'corresponsableIndicador3ID':datos['corresponsableIndicador3ID'],
                    'corresponsableIndicador3':datos['corresponsableIndicador3'],
                    'corresponsableIndicador4ID':datos['corresponsableIndicador4ID'],
                    'corresponsableIndicador4':datos['corresponsableIndicador4'],
                    'corresponsableIndicador5ID':datos['corresponsableIndicador5ID'],
                    'corresponsableIndicador5':datos['corresponsableIndicador5'],
                    
                    'evidencia_numeral': datos['evidencia_numeral'],
                    'evidencia':datos['evidencia'],
                    'evidenciaID':datos['evidenciaID'],
                    'periodoAcademico': "",  
                    'periodoAcademicoID': "", 
                    'estado_documento':"0",
                    'observacion_documento':""
                      
                                   
                })
            for documentos_i in documentos:
                periodo = documentos_i.periodoAcademico
                periodoAcademico_id = periodo.id if periodo else None
                periodoAcademico = f"{periodo.nombre}" if periodo else ""
                                
    
                data2.append({
                    'modelo':datos['modelo'],
                    'criterio':datos['criterio'],
                    'subcriterio':datos['subcriterio'],
                    'indicador_numeral':datos['indicador_numeral'],
                    'indicador':datos['indicador'],
                    'responsableIndicadorID':datos['responsableIndicadorID'],
                    'responsableIndicador': datos['responsableIndicador'],
                    'corresponsableIndicador1ID':datos['corresponsableIndicador1ID'],
                    'corresponsableIndicador1':datos['corresponsableIndicador1'],
                    'corresponsableIndicador2ID':datos['corresponsableIndicador2ID'],
                    'corresponsableIndicador2':datos['corresponsableIndicador2'],
                    'corresponsableIndicador3ID':datos['corresponsableIndicador3ID'],
                    'corresponsableIndicador3':datos['corresponsableIndicador3'],
                    'corresponsableIndicador4ID':datos['corresponsableIndicador4ID'],
                    'corresponsableIndicador4':datos['corresponsableIndicador4'],
                    'corresponsableIndicador5ID':datos['corresponsableIndicador5ID'],
                    'corresponsableIndicador5':datos['corresponsableIndicador5'],
                    
                    'evidencia_numeral': datos['evidencia_numeral'],
                    'evidencia':datos['evidencia'],
                    'evidenciaID':datos['evidenciaID'],
                    'documento':documentos_i.nombre, 
                    'documentoID':documentos_i.id,
                    'archivo': str(documentos_i.archivo),
                    'link':documentos_i.link,
                    'responsable': documentos_i.responsable.first_name +' '+ documentos_i.responsable.last_name,    
                    'responsableID': documentos_i.responsable.id, 
                    'periodoAcademico': periodoAcademico, 
                    'periodoAcademicoID': periodoAcademico_id,
                    'estado_documento':documentos_i.estado,
                    'observacion_documento':documentos_i.observacion  
                                 
                })
           
        
        return Response(data2)
    
    
        
class Evaluacion_evidencia_fil_responsable(APIView):
    def get(self, request):
        data = []
        responsable_id = request.query_params.get('responsable_id', None)
        documentos = DocumentoEvaluacion.objects.filter(responsable=responsable_id).order_by('numeral')
        for documentos_i in documentos:
            evidencias = EvidenciaEvaluacion.objects.filter(id=documentos_i.evidenciaEvaluacion.id)
            for evidencias_i in evidencias:
                indicadores = IndicadorEvaluacion.objects.filter(id=evidencias_i.indicadorEvaluacion.id)
                for indicadores_i in indicadores:
                    subcriterios = SubCriterioEvaluacion.objects.filter(id=indicadores_i.subCriterioEvaluacion.id)
                    for subcriterios_i in subcriterios:
                        criterios = CriterioEvaluacion.objects.filter(id=subcriterios_i.criterioEvaluacion.id)
                        for criterios_i in criterios:
                            periodo = documentos_i.periodoAcademico
                            periodoAcademico_id = periodo.id if periodo else None
                            periodoAcademico = f"{periodo.nombre}" if periodo else ""
                            data.append({      
                                'documento':documentos_i.nombre, 
                                'documentoID':documentos_i.id,
                                'archivo': str(documentos_i.archivo),
                                'link':documentos_i.link,
                                'responsable': documentos_i.responsable.first_name +' '+ documentos_i.responsable.last_name,    
                                'responsableID': documentos_i.responsable.id, 
                                'periodoAcademico': periodoAcademico, 
                                'periodoAcademicoID': periodoAcademico_id, 
                                'evidencia_numeral': evidencias_i.numeral,
                                'evidencia':evidencias_i.nombre,
                                'indicador_numeral':indicadores_i.numeral,
                                'indicador':indicadores_i.nombre,  
                                'responsableIndicador':f"{indicadores_i.responsable.first_name} {indicadores_i.responsable.last_name}",  
                                'subcriterio':subcriterios_i.nombre,   
                                'criterio':criterios_i.nombre,
                                'estado_documento':documentos_i.estado,
                                'observacion_documento':documentos_i.observacion, 
                                   
                                })
                        
        

        
        return Response(data)




class CriterioEvaluacion_ViewSet(viewsets.ModelViewSet):
    queryset = CriterioEvaluacion.objects.all().order_by('-id')
    serializer_class = criteriosEvaluacion_Serializer
    router = routers.DefaultRouter()
    
class DocumentosEvaluacion_ViewSet(viewsets.ModelViewSet):
    queryset = DocumentoEvaluacion.objects.all().order_by('-id')
    serializer_class = documentosEvaluacion_Serializer
    router = routers.DefaultRouter()

@api_view(['DELETE'])
def deleteArchivoEvaluacion(request):
        data = request.data
        try:
            # Obtén el documento por su ID
            documento = DocumentoEvaluacion.objects.get(id=data['documentoID'])
        except DocumentoEvaluacion.DoesNotExist:
            return Response({"message": "Documento no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        # Elimina el archivo del sistema de archivos
        documento.archivo.delete()
        # Elimina la entrada de la base de datos
        #documento.delete()
        return Response({"message": "Documento eliminado exitosamente"})


class PeriodoAcademico_ViewSet(viewsets.ModelViewSet):
    queryset = PeriodoAcademico.objects.all().order_by('-id')
    serializer_class = periodoAcademico_Serializer
    router = routers.DefaultRouter()
    
    
class Estadisticas(APIView):
    def get(self, request):
        toatal_documentos = DocumentoEvaluacion.objects.count()
        documentos_con_pdf = DocumentoEvaluacion.objects.filter(archivo__isnull=True).count()
        
        indicadores = IndicadorEvaluacion.objects.all()
        data = []
        
        for indicador_i in indicadores:
            evidencias = indicador_i.evidencias.all()
            total_documentos_indicador = DocumentoEvaluacion.objects.filter(evidenciaEvaluacion__in=evidencias).count()
            total_documentos_pdf = DocumentoEvaluacion.objects.filter(evidenciaEvaluacion__in=evidencias).exclude(
                Q(archivo__isnull=True) | Q(archivo__exact='')
                ).count()
            
            total_documentos_link = DocumentoEvaluacion.objects.filter(
                evidenciaEvaluacion__in=evidencias
                ).exclude(
                     Q(link__isnull=True) | Q(link__exact='')
                ).count()
            
            if total_documentos_indicador != 0:
                cumplimiento = ((total_documentos_pdf+total_documentos_link)/total_documentos_indicador)*100
            else:
                cumplimiento = 0
            data.append({
                'indicador':indicador_i.nombre,
                'indicadorResponsable':f"{indicador_i.responsable}",
                'total_documentos_indicador':total_documentos_indicador,
                'total_documentos_pdf': total_documentos_pdf,
                'total_documentos_link': total_documentos_link,
                'cumplimiento':cumplimiento,
            })
            
    
        
        contexto = {
            'total_documentos': toatal_documentos,
            'documentos_con_pdf':documentos_con_pdf
        }
        return Response(data)
