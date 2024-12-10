import React from "react";
import {
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  IconButton,
} from "@mui/material";
import { Edit, Delete } from "@material-ui/icons";
import { AdresseIp } from "../RapportType";

interface AdresseIpTableProps {
  adresses: AdresseIp[];
  onEdit: (adresse: AdresseIp) => void;
  onDelete: (adresseId: number) => void;
}

const AdresseIpTable = (props: AdresseIpTableProps) => {
    const { adresses, onEdit, onDelete } = props;
  return (
    <TableContainer component={Paper}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Adresse</TableCell>
            <TableCell>Statut</TableCell>
            <TableCell>Edition</TableCell>
            <TableCell>Suppression</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {adresses.map((adresse) => (
            <TableRow key={adresse.id}>
              <TableCell>{adresse.ip_address}</TableCell>
              <TableCell>{adresse.status ? "Actif" : "Inactif"}</TableCell>
              <TableCell>
                <IconButton color="primary" onClick={() => onEdit(adresse)}>
                  <Edit />
                </IconButton>
              </TableCell>
              <TableCell>
                <IconButton color="error" onClick={() => onDelete(adresse.id)}>
                  <Delete />
                </IconButton>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default AdresseIpTable;
