select a.ID, a.GENOTYPE, b.GENOTYPE as PARENT_GENOTYPE
from ECOLI_DATA a
inner join ECOLI_DATA b
on b.ID = a.PARENT_ID
where (a.GENOTYPE | b.GENOTYPE) = a.GENOTYPE
order by ID;