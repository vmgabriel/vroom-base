# VRoom Routing - Base Project
[![Built with Spacemacs](https://cdn.rawgit.com/syl20bnr/spacemacs/442d025779da2f62fc86c2082703697714db6514/assets/spacemacs-badge.svg)](http://spacemacs.org)

## Description
Using [vroom](https://github.com/VROOM-Project/vroom "vroom") Optimization Machine, for use of geo-referenzing.

Support types of problems.

### Supported problem types
- TSP (travelling salesman problem)
- CVRP (capacitated VRP)}
- VRPTW (VRP with time windows)
- MDHVRPTW (multi-depot heterogeneous vehicle VRPTW)
- PDPTW (pickup-and-delivery problem with TW)

For control of module.

Build by verso the optimization api is build for better the experience of location and manage, control of route optimization
see [verso route optimization](https://blog.verso-optim.com/category/route-optimization/api/ "Verso optimization")

For determinate the cost effective of routes, flexibility of time and location. including in driver's several task.

This have several routing engines.

- OSRM
- OpenRoutesService

Things:
- The expected order for all coordinates arrays is [lon, lat]
- all timings are in seconds
- all distances are in meters
- a *time_window* object is a pair of timestamps in the form [start, end]
- deprecated keys are crossed out
- *cost* values in output are the one used in the optimization objective
- a "task" is either a job, a pickup or a delivery

Solving Mode
Default VRP: The default solgin mode takes as input the description of a vehicle routing problem and outputs a set of routes matching all constraints

### VRoom Demo Server
[http://solver.vroom-project.org](http://solver.vroom-project.org "Demo Server for vroom")

The Demo server is configured here as way of test

### VRoom Docker Image
This include all dependencies and projects needed to successfully run an instance of vroom.

## Members
- **Gabriel Vargas Monroy**(vmgabriel)

## Initialize
For load test:

```bash
curl --header "Content-Type:application/json" --data '{"vehicles":[{"id":0,"start":[2.3526,48.8604],"end":[2.3526,48.8604]}],"jobs":[{"id":0,"location":[2.3691,48.8532]},{"id":1,"location":[2.2911,48.8566]}],"options":{"g":true}}' http://solver.vroom-project.org
```

This load

```json
{
  "routes": [
    {
      "geometry": "o`fiHaqjMBOPFrAn@p@XJFzBbAp@Xx@\\JDHDlCjAJDFBERGXQ|@CHk@lCSbAAFIZe@rBk@dCAHI\\ENCL[rACRENw@jDADI^i@~BAFCN_@bBOj@AFERi@~BAFI\\G`@Qr@ADETGRq@|CAFIZI^Kd@m@hCADELIVAFOf@Mj@CHm@tCa@fBAFIXaCnKGZOn@I\\WhAm@hCAFABGVETIZEReAvEAFGRuAjGCHAFI\\ETOp@ADKb@EPKf@GR}@`EAFGVs@`DqBbJCHMh@Ot@_AdEu@dDCHERw@jDKjAAD?DA^?P?@?J{@dEAJNjAdAdCHRx@l@HF`Al@dBfAHBF?jACd@ARNFDFBXRJF@@B@B@jFnDFD@@DBJFMt@CFYxAAVCn@ANAT?V?nCB|H?Z@x@?J?n@@n@DtB?P@l@?t@?v@?b@?V@rC@TBPFl@Jz@Hx@Fb@@J?b@Bf@?H?|@@h@@rADfGDrF@xD@f@@X?f@FtK?J?bA?F?dA?F?^AJ?HA\\@dADv@?J?HDhBFrAFz@Dl@V~BD\\L~@X|A`@nB~@|C`AfChAhBNXjBjDnCpEhBvCtCxEx@|@`AjAHUV]`@w@Tc@Ub@a@v@W\\ITUaAq@oAcE{GOW]k@OUcGoJUa@QY_AaB_@y@g@kA{@}Cc@qBYgBIi@QsAKiAEg@G_AGiAEiB?C?GCy@CmAG[ACAIKi@?G?eA?G?cA?KGuK?g@AYAg@AyDEsFEgGAsAAi@?}@?ICg@?c@AKGc@Iy@K{@Gm@CQAUAsC?W?c@?w@?u@Am@?QEuBAo@?o@?KAy@?[C}H?oC?W@U@OZ_AZwA@ILm@Ps@HWHSHITW\\]JMHItAuALM\\[LMb@_@vCiC`@_@RQp@o@FGjBgBFIPORQ`A}@POjAgARQFGx@w@tBoBZ[pB{Cr@gAHSHYHU~@kCDKHY|@mClAqGHa@BM~@qEDYXwBT{ADWVkBXiBPcA@MHi@RiAFi@Lw@N_AD[`@iCFa@BMN}@b@qCLw@BOBUTwAFg@DSb@mC@MDYHi@L{@\\yB@E@GPgAt@cFXeBBOj@qDBOBSBMPgAPkAXsBT{ATwAD]DYJu@Jo@Jq@j@oDF]BSLs@Hg@DUJs@Lw@BMLu@PqA@EF]\\yBBMBQDWBoADgC?e@@UBsB@q@@a@?a@FyD@k@@O@]B_A@s@AgA@uA@a@?a@BcBA_@Ic@qBsJGWCOCIOs@Q{@I_@Ic@GUG[{@kEACAGGWa@uBCOKe@S}@EQEWQw@[sACKG[CIeBwIAAAKEQQy@Qy@COG]Ou@Kg@CMCMQw@AEY{AKk@EMQ}@OMYKCASGMIWMOMIUAUqAPc@HO@OBUDC?[Fk@HYDuARaALMBI@WFOBYDyATw@JIBM@YDQB]Fi@HMBK@g@J_CZKBi@HsAR[FSBa@FUBKBK@]FK@]F_ALODa@DYFqARc@FE@I@mAROBSBe@HOB_BV_@FWJm@Zi@VMFGBkCrAg@XWLWLA@u@^[PGBcB~@UL}@`@UHMCCAYj@]n@_AhBEJCDa@x@GJEHPh@?@HVFV`AdDFTThALt@Hf@\\|B@LBLBPPpAdAtHF`@Lz@BPF^DVNdAFb@Fb@Jp@@JLx@Lx@DXP@J@B?DBz@^JDNHnAj@HBJFnAh@HDHDxAp@FBJFx@^PHJBNH|BbAl@VB@\\N^P`@PJDJDFBp@Z`Bt@CN",
      "violations": [],
      "steps": [
        {
          "distance": 0,
          "violations": [],
          "duration": 0,
          "arrival": 0,
          "waiting_time": 0,
          "service": 0,
          "location": [
            2.3526,
            48.8604
          ],
          "type": "start"
        },
        {
          "distance": 5599,
          "violations": [],
          "duration": 499,
          "arrival": 499,
          "job": 1,
          "waiting_time": 0,
          "service": 0,
          "id": 1,
          "location": [
            2.2911,
            48.8566
          ],
          "type": "job"
        },
        {
          "distance": 12209,
          "violations": [],
          "duration": 1126,
          "arrival": 1126,
          "job": 0,
          "waiting_time": 0,
          "service": 0,
          "id": 0,
          "location": [
            2.3691,
            48.8532
          ],
          "type": "job"
        },
        {
          "distance": 15073,
          "violations": [],
          "duration": 1472,
          "arrival": 1472,
          "waiting_time": 0,
          "service": 0,
          "location": [
            2.3526,
            48.8604
          ],
          "type": "end"
        }
      ],
      "distance": 15073,
      "priority": 0,
      "waiting_time": 0,
      "duration": 1472,
      "service": 0,
      "cost": 1472,
      "vehicle": 0
    }
  ],
  "unassigned": [],
  "summary": {
    "computing_times": {
      "routing": 2,
      "solving": 0,
      "loading": 4
    },
    "violations": [],
    "distance": 15073,
    "priority": 0,
    "waiting_time": 0,
    "duration": 1472,
    "service": 0,
    "unassigned": 0,
    "cost": 1472
  },
  "code": 0
}
```
