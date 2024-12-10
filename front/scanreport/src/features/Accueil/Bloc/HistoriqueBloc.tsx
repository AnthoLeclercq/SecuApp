import { Button, Container, Grid, Typography } from "@mui/material";
import React, { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import RapportTable from "../table/RapportTable";
import { Rapport } from "../RapportType";
import { colors } from "features/colors";
import { getReports, deleteReports } from "../RapportApi";


const HistoriqueBloc = () => {
  const dispatch = useDispatch();
  const [dateDernierSync, setDateDernierSync] = useState<Date>(new Date());
  const [listRapports, setListRapports] = useState<Rapport[]>([]);

  function openRapport(rapport: Rapport){
    window.open("http://localhost:5001/reports/download/"+rapport.id, '_blank')!.focus();
  }

  function fctLoadRapport(data: Rapport[]){
    if(data){
      setListRapports(data)
    }
  }

  function init(){
    setDateDernierSync(new Date())
    dispatch<any>(getReports(fctLoadRapport))
  }

  function fctSuppressionRapport(rapportId: number){
    dispatch<any>(deleteReports(rapportId,init))
  }

  useEffect(() => {
    init()
  }, []);

  return (
    <Container>
      <Grid container alignItems="center">
        <Grid item xs={10}>
          <Typography variant="h5" sx={{fontFamily: "Roboto"}} mt={2} align="left" gutterBottom >
            Historique des rapports : 
          </Typography>
        </Grid>
        <Grid item xs={2} style={{textAlign: "right"}}>
            <Button variant="contained" onClick={init}>
                Actualiser
            </Button>
        </Grid>
        <Grid item xs={12}>
          <Typography sx={{fontFamily: "Roboto", fontSize: "80%"}} color={colors.primary} align="right" mb={2} gutterBottom >
            {`Dernière actualisation : ${dateDernierSync.toLocaleDateString()} ${dateDernierSync.getHours()}:${dateDernierSync.getMinutes()}:${dateDernierSync.getSeconds()<10 ? "0"+dateDernierSync.getSeconds():dateDernierSync.getSeconds()}`}
          </Typography>
        </Grid>
        <Grid item xs={12} >
          <RapportTable rapports={listRapports} openRapport={openRapport} onDelete={fctSuppressionRapport}  />
        </Grid>
      </Grid>
    </Container>
  );
}

export default HistoriqueBloc;
