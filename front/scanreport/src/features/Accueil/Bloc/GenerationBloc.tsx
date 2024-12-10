import { Button, Container, Divider, Grid, LinearProgress, Paper, Typography } from "@mui/material";
import { colors } from "features/colors";
import React, { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import AnalyseBloc from "./AnalyseBloc";
import { Security } from "@material-ui/icons";
import { scanGlobalApi, scanPortsApi, scanServicesApi, scanVulnerabilitiesApi } from "../RapportApi";
import { toast } from "react-toastify";

const GenerationBloc = () => {
    const dispatch = useDispatch();
    const [scanGlobal, setScanGlobal] = useState<number>(0);
    const [scanGlobalDisable, setScanGlobalDisable] = useState<boolean>(false);
    const [scanVuln, setScanVuln] = useState<number>(0);
    const [scanPorts, setScanPorts] = useState<number>(0);
    const [scanServices, setScanServices] = useState<number>(0);

    function globalScanStatut(statut: number){
        setScanGlobal(statut)
        setScanVuln(statut)
        setScanPorts(statut)
        setScanServices(statut)
    }

    function successGlobal(data: any){
        globalScanStatut(2)
        if(data && data[0] && data[0].error){
            toast.error("Un scan est déjà en cours")
            globalScanStatut(0)
        }
    }

    function globalAnalyse() {
        console.log("analyse")
        globalScanStatut(1)
        dispatch<any>(scanGlobalApi(successGlobal))
    }

    function successVulnerabilities(data: any) {
        setScanVuln(2)
        if(data && data[0] && data[0].error){
            toast.error("Un scan est déjà en cours")
            setScanVuln(0)
        }
    }

    function successPorts(data: any) {
        setScanPorts(2)
        if(data && data[0] && data[0].error){
            toast.error("Un scan est déjà en cours")
            setScanPorts(0)
        }
    }

    function successServices(data: any) {
        setScanServices(2)
        if(data && data[0] && data[0].error){
            toast.error("Un scan est déjà en cours")
            setScanServices(0)
        }
    }

    function vulnerabilities() {
        setScanVuln(1)
        dispatch<any>(scanVulnerabilitiesApi(successVulnerabilities))
    }

    function ports() {
        setScanPorts(1)
        dispatch<any>(scanPortsApi(successPorts))
    }

    function services() {
        setScanServices(1)
        dispatch<any>(scanServicesApi(successServices))
    }


    useEffect(() => {
        const currentScan = scanPorts === 1 || scanGlobal === 1 || scanVuln === 1 || scanServices === 1;
        if(currentScan){
            setScanGlobalDisable(true)
        }else{
            setScanGlobalDisable(false)
        }
    }, [scanPorts, scanGlobal, scanVuln, scanServices]);

    return (
        <Container>
            <Grid container alignItems="center">
                <Grid item xs={12} mt={3}>
                    <Paper elevation={2} sx={{ backgroundColor: "#63A37569",opacity: scanGlobalDisable ? 0.8 : 1,  padding: 2 }}>
                        <Grid container alignItems="center">
                            <Grid item xs={1}>
                                <Security htmlColor="#c25200" fontSize="large" />
                            </Grid>
                            <Grid item xs={6}>
                                <Typography variant="h5" sx={{ fontFamily: "Roboto" }} align="left" my={2} gutterBottom >
                                    Lancer une analyse complète des cibles
                                </Typography>
                            </Grid>
                            <Grid item xs={5} style={{ textAlign: 'center' }}>
                                <Button variant="contained" disabled={scanGlobalDisable} onClick={globalAnalyse}>
                                    analyse globale
                                </Button>
                            </Grid>
                        </Grid>
                    </Paper>
                </Grid>
                <Grid item xs={6} mt={4}>
                    <Typography variant="h5" sx={{ fontFamily: "Roboto", fontSize: "125%" }} align="left" my={2} gutterBottom >
                        Liste des analyses :
                    </Typography>
                </Grid>
                <Grid item xs={12}>
                    <Divider sx={{ backgroundColor: colors.primary }} />
                </Grid>
                <Grid container alignItems="center" mt={4}>
                    <Grid item mb={2} xs={12}>
                        <AnalyseBloc libelleTxt={"Scan vulnérabilités"} libelleBtn={"analyse vulnérabilités"} stateAnalyse={scanVuln} divider={true} fctClick={vulnerabilities} />
                    </Grid>
                    <Grid item mb={2} xs={12}>
                        <AnalyseBloc libelleTxt={"Scan port"} libelleBtn={"analyse port"} stateAnalyse={scanPorts} divider={true} fctClick={ports} />
                    </Grid>
                    <Grid item mb={2} xs={12}>
                        <AnalyseBloc libelleTxt={"Scan services"} libelleBtn={"analyse services"} stateAnalyse={scanServices} divider={true} fctClick={services} />
                    </Grid>
                </Grid>
            </Grid>
        </Container>
    );
}

export default GenerationBloc;
