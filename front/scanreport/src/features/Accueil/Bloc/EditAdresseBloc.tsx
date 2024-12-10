import React, { useState, FC } from 'react';
import { Button, Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle, Checkbox, TextField, Grid, Typography } from '@mui/material';
import { AdresseIp } from '../RapportType';


interface PopupProps {
  isOpen: boolean;
  adresseIp: AdresseIp;
  createMode: boolean;
  onClose: () => void;
  onSubmit: (adresseIp: AdresseIp) => void;
}

const EditAdresseBloc: FC<PopupProps> = ({ isOpen, adresseIp,createMode, onClose, onSubmit }) => {
  const [adresse, setAdresse] = useState(adresseIp.ip_address);
  const [status, setStatus] = useState(adresseIp.status === true);

  const handleSubmit = () => {
    onSubmit({ id: adresseIp.id, ip_address: adresse, status: status});
    onClose();
  };


  return (
    <Dialog open={isOpen} onClose={onClose}>
      <DialogTitle>Modifier l'adresse IP</DialogTitle>
      <DialogContent>
        <DialogContentText>
          Veuillez modifier les informations de l'adresse IP.
        </DialogContentText>
        <TextField
          autoFocus
          margin="dense"
          id="adresse-ip"
          label="Adresse IP"
          type="text"
          value={adresse}
          onChange={(e) => setAdresse(e.target.value)}
          required
        />
        <br />
        <Grid item xs={8}>
            <Typography>Actif</Typography>
        </Grid>
        <Grid item xs={4}>
            <Checkbox
            checked={status}
            onChange={() => setStatus(!status)}
            />
        </Grid>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Annuler</Button>
        <Button variant="contained" onClick={handleSubmit}>
        {createMode ? "Créer" : "Modifier"}
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default EditAdresseBloc;