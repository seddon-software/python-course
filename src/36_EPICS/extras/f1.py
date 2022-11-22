

        #!/usr/bin/env python3
        from caproto.server import pvproperty, PVGroup, ioc_arg_parser, run
        from caproto import ChannelType
        from textwrap import dedent
        import numpy as np
        import time
        from random import randrange
         
        class DummyBeamline(PVGroup):
            """
           An IOC with some PVs to simulate a beamline
         
           Each property here presents itself as a record with the expected fields
           over Channel Access.
         
           For ``bi`` and ``bo``, the ZNAM and ONAM fields hold the string equivalent
           values for 0 and 1.  These are derived from the ``enum_strings`` keyword
           argument.
         
           That is, ``bo.ZNAM`` is "Zero Value", ``bo.ONAM`` is ``"One Value"``, such
           that ``caput bo 1`` would show it being set to ``"One Value"``.
         
           For the mbbi record, the ``ZRST`` (zero string) field, ``ONST`` (one
           string) field, and so on (up to 15), are similarly respected and mapped
           from the ``enum_strings`` keyword argument.
         
           Scalar PVs
           ----------
           bo (enum) - a binary output (bo) record
           bi (enum) - a binary input (bi) record
           mbbi (enum) - a multi-bit binary input (mbbi) record
           """
         
            shutter = pvproperty(value='Closed',
                            enum_strings=['Closed', 'Opened'],
                            record='bo',
                            dtype=ChannelType.ENUM)
         
            @shutter.scan(period=90)
            async def shutter(self,instance,async_lib):
                position = randrange(2)
                await instance.write(value=position)
           
            feedback = pvproperty(value='1',
                            enum_strings=['0', '1'],
                            record='bi',
                            dtype=ChannelType.ENUM)
         
            @feedback.scan(period=180)
            async def feedback(self,instance,async_lib):
                fbstatus = randrange(2)
                await instance.write(value=fbstatus)
           
            detector = pvproperty(value='Idle',
                              enum_strings=['Idle',
                                            'Acquire',
                                            'Arming',
                                            'Aborted',
                                            'Error'],
                              record='mbbi',
                              dtype=ChannelType.ENUM
                              )
         
            @detector.scan(period=30)
            async def detector(self,instance,async_lib):
                detstatus = randrange(5)
                await instance.write(value=detstatus)
           
            current = pvproperty(value=295, dtype=float, read_only=True)
         
            @current.scan(period=60)
            async def current(self, instance, async_lib):
                current = 295 + 11 * np.sin(time.monotonic() * (2 * np.pi) / 4)
                await instance.write(value=current)
               
            temperature = pvproperty(value=20, dtype=float, read_only=True)
         
            #Maybe use this temperature decay example later https://github.com/caproto/caproto/blob/master/caproto/ioc_examples/thermo_sim.py
            @temperature.scan(period=20)
            async def temperature(self, instance, async_lib):
                temp = 20 + 5.2 * np.sin(time.monotonic() * (2 * np.pi) / 4)
                await instance.write(value=temp)
         
            filepath = pvproperty(
                name='FileName_RBV',
                value='/dls/i04/data/2020/mx25233-11/hPGK1/hPGK1_2KMME_TerF3/hPGK1_2KMME_TerF3_2_master.h5',
                max_length=256)
         
            paths_list = ['/dls/i04/data/2020/mx25233-11/hPGK1/hPGK1_2KMME_TerF3/hPGK1_2KMME_TerF3_01_master.h',
                          '/dls/i04/data/2020/mx25233-11/hPGK1/hPGK1_2KMME_TerF3/hPGK1_2KMME_TerF3_02_master.h',
                          '/dls/i04/data/2020/mx25233-11/hPGK1/hPGK1_2KMME_TerF3/hPGK1_2KMME_TerF3_03_master.h',
                          '/dls/i04/data/2020/mx25233-11/hPGK1/hPGK1_2KMME_TerF3/hPGK1_2KMME_TerF3_04_master.h',
                          '/dls/i04/data/2020/mx25233-11/hPGK1/hPGK1_2KMME_TerF3/hPGK1_2KMME_TerF3_05_master.h',
                          '/dls/i04/data/2020/mx25233-11/hPGK1/hPGK1_2KMME_TerF3/hPGK1_2KMME_TerF3_06_master.h',
                          '/dls/i04/data/2020/mx25233-11/hPGK1/hPGK1_2KMME_TerF3/hPGK1_2KMME_TerF3_07_master.h',
                          '/dls/i04/data/2020/mx25233-11/hPGK1/hPGK1_2KMME_TerF3/hPGK1_2KMME_TerF3_08_master.h',
                          '/dls/i04/data/2020/mx25233-12/hPGK1/hPGK1_2KMME_TerF3/hPGK1_2KMME_TerF3_09_master.h',
                          '/dls/i04/data/2020/mx25233-13/hPGK1/hPGK1_2KMME_TerF3/hPGK1_2KMME_TerF3_10_master.h',
                          ]
           
            @filepath.scan(period=180)
            async def filepath(self, instance, async_lib, paths_list=paths_list):
                new_path = paths_list[randrange(10)]
                await instance.write(value=new_path)
         
            # Values of CS-CS-MSTAT-01:MODE
            modes = ['Shutdown',
                     'Injection',
                     'Mach. Dev.',
                     'No Beam',
                     'User',
                     'Special',
                     'BL Startup',
                     'Unknown']
         
            mode = pvproperty(name='machine_mode',
                              value='User',
                              record='mbbi',
                              enum_strings=modes,
                              dtype=ChannelType.ENUM)
         
            @mode.scan(period=120)
            async def mode(self, instance, async_lib, ):
                new_mode = randrange(8)
                await instance.write(value=new_mode)
         
        if __name__ == '__main__':
            ioc_options, run_options = ioc_arg_parser(
                default_prefix='dummy:beamline:',
                desc=dedent(DummyBeamline.__doc__))
            ioc = DummyBeamline(**ioc_options)
            run(ioc.pvdb, **run_options)
         

