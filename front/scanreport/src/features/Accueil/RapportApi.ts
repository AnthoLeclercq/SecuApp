import { fetchApi } from "features/rest";
import { toast } from "react-toastify";
import { AdresseIp, Rapport } from "./RapportType";

export const createAddress = (data: any, funcSuccess: () => void) => async (dispatch: any) => {
    try {
      fetchApi({
        method: 'POST',
        endpoint: '/ip-addresses',
        data: data,
        funcSuccess: () => {
          funcSuccess();
        },
        dispatch
      });
    } catch (err) {
      toast.error('Une erreur s\'est produite. Veuillez réessayer.');
    }
  };


  export const getAdresse = (funcSuccess: (data: AdresseIp[]) => void) => async (dispatch: any) => {
    try {
      fetchApi({
        method: 'GET',
        endpoint: '/ip-addresses',
        funcSuccess: (data) => {
          funcSuccess(data.ip_addresses);
        },
        dispatch
      });
    } catch (err) {
      toast.error('Une erreur s\'est produite. Veuillez réessayer.');
    }
  };

  export const deleteAdresse = (id: number,funcSuccess: () => void) => async (dispatch: any) => {
    try {
      fetchApi({
        method: 'DELETE',
        endpoint: '/ip-addresses/'+id,
        funcSuccess: () => {
          funcSuccess();
        },
        dispatch
      });
    } catch (err) {
      toast.error('Une erreur s\'est produite. Veuillez réessayer.');
    }
  };

  export const editAdresse = (data: AdresseIp, funcSuccess: () => void) => async (dispatch: any) => {
    try {
      fetchApi({
        method: 'PUT',
        endpoint: '/ip-addresses/'+data.id,
        data: data,
        funcSuccess: () => {
          funcSuccess();
        },
        dispatch
      });
    } catch (err) {
      toast.error('Une erreur s\'est produite. Veuillez réessayer.');
    }
  };

  export const scanVulnerabilitiesApi = (funcSuccess: (data: any) => void) => async (dispatch: any) => {
    try {
      fetchApi({
        method: 'GET',
        endpoint: '/vulnerabilities/scan',
        showLoader: false,
        funcSuccess: (data) => {
          funcSuccess(data);
        },
        dispatch
      });
    } catch (err) {
      toast.error('Une erreur s\'est produite. Veuillez réessayer.');
    }
  };

  export const scanPortsApi = (funcSuccess: (data: any) => void) => async (dispatch: any) => {
    try {
      fetchApi({
        method: 'GET',
        endpoint: '/ports/scan',
        showLoader: false,
        funcSuccess: (data) => {
          funcSuccess(data);
        },
        dispatch
      });
    } catch (err) {
      toast.error('Une erreur s\'est produite. Veuillez réessayer.');
    }
  };

  export const scanServicesApi = (funcSuccess: (data: any) => void) => async (dispatch: any) => {
    try {
      fetchApi({
        method: 'GET',
        endpoint: '/services/scan',
        showLoader: false,
        funcSuccess: (data) => {
          funcSuccess(data);
        },
        dispatch
      });
    } catch (err) {
      toast.error('Une erreur s\'est produite. Veuillez réessayer.');
    }
  };

  export const scanGlobalApi = (funcSuccess: (data: any) => void) => async (dispatch: any) => {
    try {
      fetchApi({
        method: 'GET',
        endpoint: '/analysis/scan',
        showLoader: false,
        funcSuccess: (data) => {
          funcSuccess(data);
        },
        dispatch
      });
    } catch (err) {
      toast.error('Une erreur s\'est produite. Veuillez réessayer.');
    }
  };
  
  export const getReports = (funcSuccess: (data: Rapport[]) => void) => async (dispatch: any) => {
    try {
      fetchApi({
        method: 'GET',
        endpoint: '/reports',
        funcSuccess: (data) => {
          funcSuccess(data.reports);
        },
        dispatch
      });
    } catch (err) {
      toast.error('Une erreur s\'est produite. Veuillez réessayer.');
    }
  };

  export const deleteReports = (id: number, funcSuccess: () => void) => async (dispatch: any) => {
    try {
      fetchApi({
        method: 'DELETE',
        endpoint: '/reports/'+id,
        funcSuccess: () => {
          funcSuccess();
        },
        dispatch
      });
    } catch (err) {
      toast.error('Une erreur s\'est produite. Veuillez réessayer.');
    }
  };