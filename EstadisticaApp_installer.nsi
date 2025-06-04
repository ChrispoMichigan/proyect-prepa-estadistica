; Script de instalación personalizado para EstadisticaApp

; Definiciones
!define APPNAME "Distribuciones Estadisticas"
!define COMPANYNAME "Proyecto Estadistica Preparatoria"
!define DESCRIPTION "Herramienta educativa para calculos de distribuciones Z y t"
!define VERSIONMAJOR 1
!define VERSIONMINOR 0
!define VERSIONBUILD 0

; URLs
!define ABOUTURL "https://github.com/ChrispoMichigan"

; Información del archivo ejecutable
OutFile "EstadisticaApp_Setup.exe"
InstallDir "$PROGRAMFILES\EstadisticaApp"
Name "${APPNAME}"
Caption "Instalacion de ${APPNAME}"
BrandingText "Proyecto Estadistica Preparatoria"

; Solicitar privilegios de administrador
RequestExecutionLevel admin

; Incluir librerías modernas
!include "MUI2.nsh"
!include "WinVer.nsh"
!include "FileFunc.nsh"

; Definir la interfaz gráfica
!define MUI_ABORTWARNING
!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\modern-install.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\modern-uninstall.ico"
!define MUI_WELCOMEFINISHPAGE_BITMAP "${NSISDIR}\Contrib\Graphics\Wizard\win.bmp"
!define MUI_UNWELCOMEFINISHPAGE_BITMAP "${NSISDIR}\Contrib\Graphics\Wizard\win.bmp"

; Textos personalizados
!define MUI_WELCOMEPAGE_TITLE "Asistente de Instalacion de ${APPNAME}"
!define MUI_WELCOMEPAGE_TEXT "Este programa instalara ${APPNAME} en su ordenador.$\r$\n$\r$\nSe recomienda que cierre todas las demas aplicaciones antes de iniciar la instalacion. Esto hara posible actualizar archivos relacionados con el sistema sin tener que reiniciar su ordenador.$\r$\n$\r$\nPresione Siguiente para continuar."

!define MUI_FINISHPAGE_TITLE "Instalacion completada"
!define MUI_FINISHPAGE_TEXT "${APPNAME} ha sido instalado correctamente en su computadora."
!define MUI_FINISHPAGE_RUN "$INSTDIR\EstadisticaApp.exe"
!define MUI_FINISHPAGE_RUN_TEXT "Ejecutar ${APPNAME} ahora"
!define MUI_FINISHPAGE_LINK "Creador"
!define MUI_FINISHPAGE_LINK_LOCATION "${ABOUTURL}"

; Páginas del instalador (eliminada la página de licencia)
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

; Páginas del desinstalador
!insertmacro MUI_UNPAGE_WELCOME
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH

; Configuración del idioma
!insertmacro MUI_LANGUAGE "Spanish"

; Verificación de requisitos al iniciar
Function .onInit
  ${IfNot} ${AtLeastWin7}
    MessageBox MB_OK|MB_ICONSTOP "Esta aplicacion requiere Windows 7 o superior."
    Abort
  ${EndIf}
FunctionEnd

; Componentes de instalación
Section "Aplicación principal" SecMain
  SectionIn RO  ; Esta seccion es requerida
  
  ; Establecer directorio de salida
  SetOutPath "$INSTDIR"
  
  ; Añadir archivos
  File /r "dist\EstadisticaApp\*.*"
  
  ; Crear acceso directo en el menú inicio
  CreateDirectory "$SMPROGRAMS\${APPNAME}"
  CreateShortcut "$SMPROGRAMS\${APPNAME}\${APPNAME}.lnk" "$INSTDIR\EstadisticaApp.exe"
  CreateShortcut "$SMPROGRAMS\${APPNAME}\Desinstalar.lnk" "$INSTDIR\uninstall.exe"
  
  ; Crear desinstalador
  WriteUninstaller "$INSTDIR\uninstall.exe"
  
  ; Registrar aplicación en "Programas y características" de Windows
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\EstadisticaApp" "DisplayName" "${APPNAME}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\EstadisticaApp" "UninstallString" "$\"$INSTDIR\uninstall.exe$\""
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\EstadisticaApp" "QuietUninstallString" "$\"$INSTDIR\uninstall.exe$\" /S"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\EstadisticaApp" "InstallLocation" "$\"$INSTDIR$\""
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\EstadisticaApp" "DisplayIcon" "$\"$INSTDIR\EstadisticaApp.exe$\""
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\EstadisticaApp" "Publisher" "${COMPANYNAME}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\EstadisticaApp" "URLInfoAbout" "${ABOUTURL}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\EstadisticaApp" "DisplayVersion" "${VERSIONMAJOR}.${VERSIONMINOR}.${VERSIONBUILD}"
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\EstadisticaApp" "VersionMajor" ${VERSIONMAJOR}
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\EstadisticaApp" "VersionMinor" ${VERSIONMINOR}
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\EstadisticaApp" "NoModify" 1
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\EstadisticaApp" "NoRepair" 1
  
  ; Calcular y registrar el tamaño instalado
  ${GetSize} "$INSTDIR" "/S=0K" $0 $1 $2
  IntFmt $0 "0x%08X" $0
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\EstadisticaApp" "EstimatedSize" "$0"
SectionEnd

Section "Acceso directo en el escritorio" SecDesktop
  CreateShortcut "$DESKTOP\${APPNAME}.lnk" "$INSTDIR\EstadisticaApp.exe"
SectionEnd

; Descripciones de las secciones
!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
  !insertmacro MUI_DESCRIPTION_TEXT ${SecMain} "Instala los archivos esenciales de la aplicacion."
  !insertmacro MUI_DESCRIPTION_TEXT ${SecDesktop} "Crea un acceso directo en el escritorio."
!insertmacro MUI_FUNCTION_DESCRIPTION_END

; Desinstalador
Section "Uninstall"
  ; Eliminar accesos directos
  Delete "$DESKTOP\${APPNAME}.lnk"
  Delete "$SMPROGRAMS\${APPNAME}\${APPNAME}.lnk"
  Delete "$SMPROGRAMS\${APPNAME}\Desinstalar.lnk"
  RMDir "$SMPROGRAMS\${APPNAME}"
  
  ; Eliminar archivos instalados
  RMDir /r "$INSTDIR"
  
  ; Eliminar registros de desinstalación
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\EstadisticaApp"
SectionEnd