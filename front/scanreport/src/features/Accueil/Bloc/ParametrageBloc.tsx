import { Button, Container, Grid, Typography } from "@mui/material";
import React, { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import AdresseIpTable from "../table/AdresseIpTable";
import { AdresseIp } from "../RapportType";
import EditAdresseBloc from "./EditAdresseBloc";
import { createAddress, deleteAdresse, editAdresse, getAdresse } from "../RapportApi";
import { toast } from 'react-toastify';

const ParametrageBloc = () => {
  const dispatch = useDispatch();

  const [currentIp, setCurrentIp] = useState<AdresseIp>();
  const [listeAdressesIp, setListeAdressesIp] = useState<AdresseIp[]>([]);
  const [editMode, setEditMode] = useState<boolean>(false);
  const [createMode, setCreateMode] = useState<boolean>(false);

  function fctCreateAdresse(){
    const adresse: AdresseIp = {
      id: 0,
      ip_address: "",
      status: true,
    }
    setCurrentIp(adresse)
    setCreateMode(true)
  }

  function submitCreateAdress(adresse: AdresseIp){
    const obj = {
      ip_address: adresse.ip_address,
      status: adresse.status
    }
    function success(){
      toast.success("Adresse créée avec succés")
      init()
    }
    dispatch<any>(createAddress(obj, success))
    resetAdresse()
  }

  function fctEditAdresse(adresse: AdresseIp){
    setCurrentIp(adresse)
    setEditMode(true)
  }

  function submitEditAdress(adresse: AdresseIp){
    function success(){
      toast.success("Adresse modifiée avec succés")
      init()
    }
    dispatch<any>(editAdresse(adresse, success))
    resetAdresse()
  }

  function resetAdresse(){
    setCurrentIp(undefined)
    setEditMode(false)
    setCreateMode(false)
  }

  function fctSuppressionAdresse(adresseId: number){
    function success(){
      toast.success("Adresse supprimée avec succés")
      init()
    }
    dispatch<any>(deleteAdresse(adresseId, success))
  }

  function loadList(data: AdresseIp[]){
    setListeAdressesIp([])
    if(data){
      setListeAdressesIp(data)
    }else{
      setListeAdressesIp([])
    }
  }

  function init(){
    dispatch<any>(getAdresse(loadList))
  }

  useEffect(() => {
    init()
  }, []);


  return (
    <Container>
      <Grid container alignItems="center">
        <Grid item xs={12}>
          <Typography variant="h5" sx={{fontFamily: "Roboto"}} align="left" my={2} gutterBottom >
            Parémétrage des adresses ip des cibles : 
          </Typography>
        </Grid>
        <Grid item xs={12} mb={5}>
          <Button variant="contained" onClick={fctCreateAdresse}>
              Ajouter une adresse
          </Button>
        </Grid>
        <Grid item xs={12} >
          <AdresseIpTable adresses={listeAdressesIp} onEdit={fctEditAdresse} onDelete={fctSuppressionAdresse}  />
        </Grid>
      </Grid>
      {currentIp !== undefined && (
        <EditAdresseBloc createMode={false} isOpen={editMode} adresseIp={currentIp} onClose={resetAdresse} onSubmit={submitEditAdress} />
      )}
       {currentIp !== undefined && (
        <EditAdresseBloc createMode={true} isOpen={createMode} adresseIp={currentIp} onClose={resetAdresse} onSubmit={submitCreateAdress} />
      )}
    </Container>
  );
}

export default ParametrageBloc;
